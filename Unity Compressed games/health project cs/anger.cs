using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
public class anger : MonoBehaviour
{
    public int health = 100;
    public Slider healthbar;
    // Start is called before the first frame update
    void Start()
    {
        healthbar.maxValue = health;
    }

    // Update is called once per frame
    void Update()
    {
        healthbar.value = health;
        if(health <= 0)
        {
            Destroy(this.gameObject);
        }
    }
    private void OnCollisionEnter2D(Collision2D collision)
    {
        if(collision.gameObject.tag == "arrow")
        {
            health--;
        }
    }
}
