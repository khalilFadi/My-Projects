using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class playeMovment : MonoBehaviour
{
    public float speed;
    public GameObject arrow;
    public static int health = 10;
    public Slider sli;
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        movment();
        if (Input.GetMouseButtonDown(0))
        {
            Instantiate(arrow);
        }
        sli.value = health;
        if(health <= 0)
        {
            Destroy(this.gameObject);
        }
    }
    void movment()
    {
        if (Input.GetKey("a"))
        {
            this.gameObject.transform.position += new Vector3(speed * -1, 0f, 0f);
        }
        if (Input.GetKey("d"))
        {
            this.gameObject.transform.position += new Vector3(speed * 1, 0f, 0f);
        }
        if (Input.GetKey("w"))
        {
            this.gameObject.transform.position += new Vector3(0f, speed, 0f);
        }
        if (Input.GetKey("s"))
        {
            this.gameObject.transform.position += new Vector3(0f, speed * -1, 0f);
        }
    }
}
