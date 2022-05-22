using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class fallingaction : MonoBehaviour
{
    public GameObject theFaller;
    public Collider2D[] col;
    public int speed;
    public string gameobjectag;

    private void OnTriggerEnter2D(Collider2D collision)
    {
        if(collision.gameObject.tag == gameobjectag)
        {
            StartCoroutine(fall());
        }
    }
    IEnumerator fall() {
        foreach(Collider2D collisions in col)
        {
            collisions.enabled = false;
        }


        //for (int i = 0; i < 12; i++)
        //{
        //    yield return new WaitForSeconds(0.000001f);
        //    transform.Translate(transform.up * speed * Time.deltaTime);
            
        //}
        for (int i = 0; i < 50; i++)
        {
            yield return new WaitForSeconds(0.000001f);
            transform.Translate(transform.up * -1 * speed * 4 * Time.deltaTime);

        }
    }

}
