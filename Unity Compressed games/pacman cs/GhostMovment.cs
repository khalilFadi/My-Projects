using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class GhostMovment : MonoBehaviour
{
    public int speed;
    bool wait = true;
    // Start is called before the first frame update
    void Start()
    {
        changerotation();
    }
    public float x = 0f, y = -0.01f;
    // Update is called once per frame
    float lastx, lasty;
    void Update()
    {
        transform.Translate(x, y, 0f);
        lastx = transform.position.x;
        lasty = transform.position.y;
    }
   
    private void OnCollisionEnter2D(Collision2D collision)
    {
        if(collision.gameObject.tag == "borders")
        {
            changerotation();
        }
    }
    private void OnCollisionStay2D(Collision2D collision)
    {
        if (collision.gameObject.tag == "borders" || collision.gameObject.tag == "ghost")
        {
            if (wait)
            {
                wait = false;
                StartCoroutine(checkforchange());
                changerotation();
            }
        }
    }
    int past = 2;
    void changerotation() {
        int random = Random.Range(1, 4);
        float pastx = x, pasty = y;
        
        switch (random)
        {
            case 1:
                x = 0;
                y = -0.01f;
                break;
            case 2:
                x = 0;
                y = 0.01f;
                break;
            case 3:
                x = 0.01f;
                y = 0;
                break;
            case 4:
                x = -0.01f;
                y = 0;
                break;
        }
        if(pastx == x && pasty == y)
        {
            changerotation();
        }
       

    }
    IEnumerator checkforchange()
    {
        yield return new WaitForSeconds(2.1f);
        wait = true;
    }
}
