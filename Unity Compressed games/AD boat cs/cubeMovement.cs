using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System;
public class cubeMovement : MonoBehaviour
{
    Rigidbody RB;
    public int speed;
    float slideSpeed = 0.9f;
    // Start is called before the first frame update
    void Start()
    {
        RB = this.GetComponent<Rigidbody>();
    }

    // Update is called once per frame
    void Update()
    {
        //Movment 
        if (Input.GetKey(KeyCode.A))
        {
            RB.AddForce(new Vector3(-speed, 0, 0));
        }
        if (Input.GetKey(KeyCode.D))
        {
            RB.AddForce(new Vector3(speed, 0, 0));
        }
        if (Input.GetKey(KeyCode.W))
        {
            RB.AddForce(new Vector3(0, 0, speed));
        }
        if (Input.GetKey(KeyCode.S))
        {
            RB.AddForce(new Vector3(0, 0, -speed));
        }

        //check if it goes too fast then decrease its speed 
        if (RB.velocity.magnitude > 1)
        {
            //check if each axis is bigger than zero then minus smaller than zero then plus zero then dont change 
            RB.velocity = new Vector3(
                RB.velocity.x > 0 ? RB.velocity.x - slideSpeed : RB.velocity.x < 0 ? RB.velocity.x + slideSpeed : 0,
                0, // we wan to keep the y from chaning so it wont go up and down 
                RB.velocity.z > 0 ? RB.velocity.z - slideSpeed : RB.velocity.z < 0 ? RB.velocity.z + slideSpeed : 0);
        }
        //print(RB.velocity + " " +  RB.velocity.magnitude);
    }
}
