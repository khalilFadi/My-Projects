using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class cube : MonoBehaviour
{
    public int health = 3;
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        if(health <= 0)
        {
            print("collision");
            transform.GetComponentInParent<combineCubes>().direction.Insert(
               transform.GetComponentInParent<combineCubes>().dir_num,
                ((transform.position - transform.GetComponentInParent<combineCubes>().transform.position) / transform.GetComponentInParent<combineCubes>().size));
            Destroy(this.gameObject);
        }
    }
    private void OnCollisionEnter(Collision collision)
    {
        if(collision.gameObject.tag == "bullet")
        {
            health -= 1;
            Destroy(collision.gameObject);
        }
        if(collision.gameObject.tag == "Cube")
        {
            transform.GetComponentInParent<combineCubes>().add_cube(collision.gameObject);
        }
    }
}
