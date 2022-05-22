using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Shooter : MonoBehaviour
{
    /* this wil be simple 
     * we will get the range damage and cooldown 
     * teh system will go on top of the cube and attack the id of the enemy;
     */
    public int range; public int damage;public float cooldown;
    public Vector3 offset;
    public GameObject PlayerBullet;
    bool attack = true;
    GameObject[] Enemies;
    // Start is called before the first frame update
    void Start()
    {
        Enemies = GameObject.FindGameObjectsWithTag("Enemy");
    }

    // Update is called once per frame
    void Update()
    {
        GameObject go = closestEnemies(range);
        //non of this code will run if there is no close enemy
        if(go == this.gameObject)
        {
            return;
        }
        Instantiate(PlayerBullet, transform.position + offset, transform.rotation);
    }
    IEnumerator Cooldown()
    {
        yield return new WaitForSeconds(cooldown);
        attack = true;
    }


    //this code is taken from the turret so some names may have conflicts :) 
    GameObject closestEnemies(int r)
    {
        GameObject target = this.gameObject;
        float closestPlayer = r;
        for (int i = 0; i < Enemies.Length; i++)
        {
            float Distance = Vector3.Distance(Enemies[i].transform.position, transform.position);
            if (Distance < closestPlayer)
            {
                closestPlayer = Distance;
                target = Enemies[i];
            }
        }
        return target;
    }
}
