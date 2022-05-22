using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class playerMovment : MonoBehaviour
{
    public float speed;

    public float rotspeed = 100;
    // Start is called before the first frame update
    void Start()
    {
        rotspeed = 100;
    }

    // Update is called once per frame
    void Update()
    {
        if (Input.GetKey("w"))
        {
            this.gameObject.transform.position += new Vector3(0,speed * Time.deltaTime, 0);
            changedirection(360f);
        }
        if (Input.GetKey("s"))
        {
            this.gameObject.transform.position += new Vector3(0,-1 * speed * Time.deltaTime, 0);
            changedirection(-180f);
        }
        if (Input.GetKey("d"))
        {
            this.gameObject.transform.position += new Vector3(speed * Time.deltaTime, 0, 0);
            changedirection(-90f);
        }
        if (Input.GetKey("a"))
        {
            this.gameObject.transform.position += new Vector3(-1 * speed * Time.deltaTime, 0, 0);
            changedirection( 90f);
        }
    }
    void changedirection(float z)
    {
        transform.rotation = Quaternion.RotateTowards(transform.rotation, Quaternion.Euler(0, 0, z), rotspeed * Time.deltaTime);
    }
}
