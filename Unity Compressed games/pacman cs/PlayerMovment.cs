using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.Networking;
public class PlayerMovment : NetworkBehaviour
{
    
    // Start is called before the first frame update
    void Start()
    {
        

    }
    float x, y;
    
    // Update is called once per frame
    void Update()
    {
        if (hasAuthority == false)
        {
            return;
        }
        if (Input.GetKey(KeyCode.W))
        {
            x = -0.01f;
            y = 0;

        }
        if (Input.GetKey(KeyCode.S))
        {
            x = 0.01f;
            y = 0;
 
        }
        if (Input.GetKey(KeyCode.D))
        {
            x = 0;
            y = 0.01f;

        }
        if (Input.GetKey(KeyCode.A))
        {
            x = 0;
            y = -0.01f;

        }
        transform.Translate(x, y, 0);
    }
    private void OnCollisionEnter2D(Collision2D collision)
    {
        if(collision.gameObject.tag == "ghost")
        {
            Destroy(this.gameObject);
        }
    }
}
