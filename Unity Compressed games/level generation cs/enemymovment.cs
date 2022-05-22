using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class enemymovment : MonoBehaviour
{
    public int speed, i = 1;
    bool check = true;
    // Update is called once per frame
    void Update()
    {
        transform.Translate(speed * i * Time.deltaTime, 0, 0);
    }
    private void OnCollisionEnter2D(Collision2D collision)
    {
        if (collision.gameObject.tag == "tube"||collision.gameObject.tag == "enemy" || collision.gameObject.tag == "Player")
        {
            if(check){
                i *= -1;
                StartCoroutine(checking());
            }
        }
    }
    private void OnTriggerEnter2D(Collider2D collision)
    {
        if(collision.gameObject.tag == "redirection")
        {
            if (check)
            {
                i *= -1;
                StartCoroutine(checking());
            }
        }
    }
    IEnumerator checking()
    {
        check = false;
        yield return new WaitForSeconds(0.2f);
        check = true;
    }
}
