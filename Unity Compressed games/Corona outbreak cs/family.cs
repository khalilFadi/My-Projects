using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using TMPro;
public class family : MonoBehaviour
{
    public int MaxX, MaxY, MinX, MinY;
    public GameObject menu;
    Vector2 destina;
    public float speed;
    public Color infection;
    Color startingcolor;
    public Material startingform;
    public SpriteRenderer SR;
    public bool infected = false;
    bool change = true;
    public GameObject canva;
    public TextMeshProUGUI timeleft;
    public int timeleftnum;
    bool changeDensity = false;
    // Start is called before the first frame update
    void Start()
    {
        startingcolor = startingform.color;
        StartCoroutine(movement());
    }
    private void Awake()
    {
        
    }
    // Update is called once per frame
    bool changingsnity = true;
    void Update()
    {
        //move towards the destination 
        this.gameObject.transform.position = Vector2.MoveTowards(this.gameObject.transform.position, destina, speed * Time.deltaTime);
        if (infected)
        {
            menu.SetActive(true);
        }
        else
        {
            SR.color = startingcolor;
            changeDensity = true;
        }
        if(changingsnity != changeDensity)
        {
            if (changeDensity)
            {
                humanSpawner.saved++;
            }
            else
            {
                humanSpawner.saved--;
            }
            changingsnity = changeDensity;
        }
        
        timeleft.text = timeleftnum.ToString();
    }
    //find a random position 
    Vector2 destination()
    {
        int randomX = Random.Range(MaxX, MinX);
        int randomY = Random.Range(MaxY, MinY);
        Vector2 destination;
        return destination = new Vector2(randomX, randomY);
    }
    //change the random position each 3 secounds
    IEnumerator movement()
    {
        while (true)
        {
            destina = destination();
            yield return new WaitForSeconds(3f);
        }
    }
    private void OnCollisionEnter2D(Collision2D collision)
    {
        if(collision.gameObject.tag == "infected" || collision.gameObject.tag=="snezer")
        {
            gameObject.tag = "infected";
            infected = true;
        }
        if (collision.gameObject.tag == "mask")
        {
            Debug.Log("untilhere");
            gameObject.tag = "human ";
        }
    }
    IEnumerator timer()
    {
        canva.SetActive(true);
        timeleftnum = 14;
        while (true)
        {
            for (int i = 0; i < 14; i++)
            {
                yield return new WaitForSeconds(1f);
                timeleftnum--;
            }
            break;
        }
        infected = false;
        canva.SetActive(false);
        this.gameObject.tag = "human ";
        change = true;
    }
    private void OnTriggerEnter2D(Collider2D collision)
    {
        if(collision.gameObject.tag == "highgel")
        {
            speed = 0.01f;
        }
    }
    private void OnTriggerExit2D(Collider2D collision)
    {
        if (collision.gameObject.tag == "highgel")
        {
            speed = 2f;
        }
    }
    private void OnParticleCollision(GameObject other)
    {
        if(other.gameObject.tag == "infected" && this.gameObject.tag != "snezer")
        {
            gameObject.tag = "infected";
            menu.SetActive(true);
            Time.timeScale = 0f;
            infected = true;
        } 
    }
}
