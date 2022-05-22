using System.Collections;
using System.Collections.Generic;
using UnityEngine; 
public class bulletsMovement : MonoBehaviour
{
    public Vector3 target;
    public int Speed;
    public int dis;
    GameObject[] player;
    // Start is called before the first frame update
    void Awake()
    {
        //get the target of the parent
        StartCoroutine(time_bomb());
        player = GameObject.FindGameObjectsWithTag("Player");
        target = closestPlayer(100000).transform.position;
    }

    // Update is called once per frame
    void Update()
    {
        int place = dis;
        this.transform.position = Vector3.MoveTowards(this.transform.position, target, Speed * Time.deltaTime);
        if (Vector3.Distance(this.transform.position, transform.parent.transform.position) > place)
        {
            Destroy(this.gameObject);
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
    IEnumerator time_bomb()
    {
        yield return new WaitForSeconds(3f);
        Destroy(this.gameObject);
    }
    private void OnCollisionEnter(Collision collision)
    {
        if(collision.gameObject.tag == "Player")
        {
            collision.gameObject.GetComponent<cube>().health -= 1;
            print("collision");
        }
    }
}
