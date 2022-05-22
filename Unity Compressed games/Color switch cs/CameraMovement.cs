using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CameraMovement : MonoBehaviour
{
    public Transform []checkpoints;
    public static int leveling = 0;
    public float speed;
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        //change checkpoints only for camera
        if (this.gameObject.name == "camera")
        {
            Vector3 n = new Vector3(checkpoints[leveling].position.x, checkpoints[leveling].position.y, checkpoints[leveling].position.z);
            this.gameObject.transform.position = Vector3.MoveTowards(this.gameObject.transform.position, n, speed);
            
        }

        //destroy checkpoints
        if(this.gameObject.tag == "checkpoint")
        {
            Destroy(this.gameObject);
        }
        if (this.gameObject.tag == "leveling")
        {

        }


    }
    IEnumerator OnCollisionEnter2D(Collision2D collision)
    {
        if(collision.gameObject.tag == "Player")
        {
            if(this.gameObject.tag == "leveling")
            {
                yield return new WaitForSeconds(0.1f);
                Destroy(this.gameObject);
            }
        }
    }
    private void OnTriggerEnter2D(Collider2D collision)
    {
        if(collision.gameObject.tag == "Player")
        {
            if(this.gameObject.tag == "change")
            {
                Destroy(this.gameObject);
            }
        }
    }
}
