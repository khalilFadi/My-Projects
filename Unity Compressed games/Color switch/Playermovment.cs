using System.Collections;
using System.Collections.Generic;
using UnityEngine;
public class Playermovment : MonoBehaviour
{
    //break
    public float breakspeed;
    //death effect
    public GameObject particleeffect;
    public Rigidbody2D rb;
    public int speed;
    //colors
    public Material []colors;
    public Renderer myColor;
    //i identified each letter in a number 
    public int color;
    // Start is called before the first frame update
    void Start()
    {
        //set defult color
        int random = Random.Range(0, 4);
        
        Time.timeScale = 0f;
        myColor.material = colors[random];
        color = random;
        color++;
    }

    // Update is called once per frame
    void Update()
    {
        //movment
    
        if (Input.GetKeyDown("space") || Input.GetKey("up"))
        {
            Time.timeScale = 1f;
            StartCoroutine(pushPull());
           // rb.AddForce(transform.up * speed);
        }
        rb.drag = 1;
    }

    private void OnCollisionEnter2D(Collision2D collision)
    {
        //check for the level
        if(collision.gameObject.tag == "leveling")
        {
            CameraMovement.leveling += 1;
        }

    }
    private void OnTriggerEnter2D(Collider2D collision)
    {
        if(collision.gameObject.tag != color.ToString() && collision.gameObject.tag != "change")
        {
            Instantiate(particleeffect, this.gameObject.transform.position, this.gameObject.transform.rotation);
            Destroy(this.gameObject);
        }
        //to check for color changing
        if(collision.gameObject.tag == "change")
        {
            int random = Random.Range(0,4);
                myColor.material = colors[random];
                color = random;
                color++;

           
        }
        Debug.Log(collision.gameObject.tag);
    }
    //the push and pull of teh balls movment
    IEnumerator pushPull()
    {
        
        rb.AddRelativeForce(transform.up * speed);
        yield return null;
        
    }
}
