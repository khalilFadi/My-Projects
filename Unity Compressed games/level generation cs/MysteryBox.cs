using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class MysteryBox : MonoBehaviour
{
    public GameObject plant;
    public Color dark;
    public Renderer RD;
    bool turnedon = true;
    private void OnCollisionEnter2D(Collision2D collision)
    {
        if(collision.gameObject.tag == "Phead")
        {
            if (turnedon)
            {
                Debug.Log("he pumped his head");
                Instantiate(plant, transform.position, transform.rotation);
                turoff();
            }
           
        }
    }

    
    void turoff()
    {
        turnedon = false;
        RD.material.color = dark;
        
    }
}
