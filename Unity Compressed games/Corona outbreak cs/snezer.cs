
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using TMPro;
public class snezer : MonoBehaviour
{
    public int MaxX, MaxY, MinX, MinY;
    public GameObject coughingsound;
    Vector2 destina;
    public GameObject snezeffect;
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
        StartCoroutine(snez());
        StartCoroutine(movement());
    }
    private void Awake()
    {
        int chance = Random.Range(0, 10);
        if (chance >= 0 && chance <= 3)
        {
            infected = true;
            this.gameObject.tag = "infected";
        }
    }
    IEnumerator coughing()
    {
        GameObject cough = Instantiate(coughingsound);
        yield return new WaitForSeconds(1f);
        Destroy(cough);
    }
    // Update is called once per frame
    bool changingsnity = true;
    void Update()
    {
        //move towards the destination 
        this.gameObject.transform.position = Vector2.MoveTowards(this.gameObject.transform.position, destina, speed * Time.deltaTime);
        if (infected)
        {
            SR.color = infection;
            if (change)
            {
                StartCoroutine(timer());
                change = false;
            }
            changeDensity = false;
        }
        else
        {
            SR.color = startingcolor;
            changeDensity = true;
        }
        if (changingsnity != changeDensity)
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
        Debug.Log(humanSpawner.saved);
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
        if (collision.gameObject.tag == "infected")
        {
            gameObject.tag = "infected";
            infected = true;
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
        
        canva.SetActive(false);
        this.gameObject.tag = "human ";
        infected = false;
        change = true;
    }
    private void OnTriggerEnter2D(Collider2D collision)
    {
        if (collision.gameObject.tag == "highgel")
        {
            speed = 0.01f;
        }
        if(collision.gameObject.tag == "mask")
        {
            canva.SetActive(false);
            this.gameObject.tag = "human ";
            infected = false;
            change = true;
        }
    }
    private void OnTriggerExit2D(Collider2D collision)
    {
        if (collision.gameObject.tag == "highgel")
        {
            speed = 2f;
        }
    }
   


IEnumerator snez()
    {
        while (true)
        {
            yield return new WaitForSeconds(2f);
            if (infected)
            {
                float z = Random.Range(0.000f, 360.00f);
                Instantiate(snezeffect, this.gameObject.transform.position, new Quaternion(0f, 0f, z, 1));
                StartCoroutine(coughing());
            }
        }
    }
}
