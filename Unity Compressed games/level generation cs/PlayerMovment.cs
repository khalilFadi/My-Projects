using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;
public class PlayerMovment : MonoBehaviour
{
    public int speed, jumpvelocity;
    public GameObject camera;
    public Rigidbody2D RB;
    public Vector3 Offset;
    public bool onTheGround = true;
    // Start is called before the first frame update
    void Start()
    {
        camera = GameObject.Find("Main Camera");
    }

    // Update is called once per frame
    float x, y;
    void Update()
    {
        transform.Translate(x * Time.deltaTime * speed, y * Time.deltaTime * speed, 0f);
        direction();
        
    }
    private void LateUpdate()
    {
        camera.transform.position =new Vector3(transform.position.x+Offset.x,Offset.y, transform.position.z + Offset.z);
    }
    void direction()
    {
        if (Input.GetKey(KeyCode.D) || Input.GetKey(KeyCode.RightArrow))
        {
            x = 0.1f;
        }else if (Input.GetKey(KeyCode.A) || Input.GetKey(KeyCode.LeftArrow))
        {
            x = -0.1f;
        }

        else
        {
            x = 0;
            y = 0;

        }
        if (Input.GetKeyDown(KeyCode.W) || Input.GetKey(KeyCode.UpArrow) || Input.GetKey(KeyCode.Space))
        {
            if (onTheGround) {
                onTheGround = false;
                StartCoroutine(moveup());
            }
            
        }

    }
    private void OnCollisionEnter2D(Collision2D collision)
    {
        if(collision.gameObject.tag == "ground")
        {
            onTheGround = true;
        }
        if(collision.gameObject.tag == "enemy")
        {
          StartCoroutine(restartlevel());
        }
        if(collision.gameObject.tag == "jump")
        {
            StartCoroutine(moveup());
        }
    }
    IEnumerator moveup()
    {
        for(int i = 0;i < 12; i++)
        {
            yield return new WaitForSeconds(0.000001f);
            transform.Translate(transform.up * jumpvelocity * Time.deltaTime);
            RB.velocity.Equals(0f);
        }
    }
    public IEnumerator restartlevel()
    {
        yield return new WaitForSeconds(0.2f);
        string currentSceneName = SceneManager.GetActiveScene().name;
        SceneManager.LoadScene(currentSceneName);
        Destroy(this.gameObject);
    }
}
