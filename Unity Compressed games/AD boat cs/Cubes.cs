using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System;
public class Cubes : MonoBehaviour
{
    Rigidbody RB;
    Rigidbody Player;
    public cubeMovement MovmentScript;
    Vector3 flag;
    // Start is called before the first frame update
    void Start()
    {
        RB = this.GetComponent<Rigidbody>();
        Player = GameObject.Find("Player").GetComponent<Rigidbody>();
        //MovmentScript = this.GetComponent<cubeMovement>();
    }

    // Update is called once per frame
    void Update()
    {

    }
    private void OnCollisionEnter(Collision collision)
    {
        if (collision.gameObject.name == "Player" && this.tag == "Cube")
        {
            //stop it from moving and make it a child for the paret
            //plus keep it following the parent RB
            Destroy(this.GetComponent<GameObject>());
            // RB.velocity = new Vector3(0, 0, 0);
            // MovmentScript.enabled = false;
            // this.tag = "Player";
            // flag = this.transform.position - Player.transform.position;
        }
    }

}
