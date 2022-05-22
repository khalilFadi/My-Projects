using System.Collections;
using System.Collections.Generic;
using UnityEngine;


public class arrowMovment : MonoBehaviour
{
    public Transform player;
    public Vector3 target;
    public float speed;
    Vector2 ray;
    // Start is called before the first frame update

    void Awake()
    {
        player = GameObject.Find("player").transform;
        this.gameObject.transform.position = player.position;
        ray = Camera.main.ScreenToWorldPoint(Input.mousePosition);
        StartCoroutine(destrucion());
    }

    // Update is called once per frame
    void Update()
    {
        
        this.gameObject.transform.position = Vector2.MoveTowards(this.gameObject.transform.position, ray, speed);
    }
    IEnumerator destrucion()
    {
        yield return new WaitForSeconds(2f);
        Destroy(this.gameObject);
    }
    private void OnCollisionEnter2D(Collision2D collision)
    {
        if (collision.gameObject.tag != "player")
        {
            Destroy(this.gameObject);
        }
        
    }
    private void OnCollisionExit2D(Collision2D collision)
    {
        if (collision.gameObject.tag != "player")
        {
            Destroy(this.gameObject);
        }

    }
}
