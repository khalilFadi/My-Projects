using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class EnemyShoot : MonoBehaviour
{
    GameObject[] player;
    public int range;
    public GameObject bullet;
    public float wooldown;
    bool cooldown = true;
    bool stop = false;
    [HideInInspector]
    public GameObject Target;
    /*the plan
     * which is to make his object shoot bullets at our player
     * we will need couple f things first
     *   the distance from the player to tower  
     *      the distance of the closest object with the tag player
     *   the bullet dirction
     */
    // Start is called before the first frame update
    void Start()
    {
        player = GameObject.FindGameObjectsWithTag("Player");
    }

    // Update is called once per frame
    void Update()
    {
        if (stop)
        {
            //return;
        }
        GameObject target = closestPlayer(range);
        if(target != this.gameObject && cooldown)
        {
            cooldown = false;
            GameObject g = Instantiate(bullet, this.transform.position, this.transform.rotation);
            g.transform.SetParent(transform);
            StartCoroutine(timer());
        }   
    }
    GameObject closestPlayer(int r)
    {
        GameObject target = this.gameObject;
        float closestPlayer = r;
        for (int i = 0; i < player.Length; i++)
        {
            float Distance = Vector3.Distance(player[i].transform.position, transform.position);
            if (Distance < closestPlayer)
            {
                closestPlayer = Distance;
                target = player[i];
            }
        }
        return target;
    }
    IEnumerator timer()
    {
        yield return new WaitForSeconds(wooldown);
        cooldown = true;
    }
}
