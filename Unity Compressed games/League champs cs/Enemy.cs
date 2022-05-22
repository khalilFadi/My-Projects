using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
public class Enemy : MonoBehaviour
{
    public Slider sli;
    public int health= 3;
    Vector3 direction;
    public int speed;
    // Start is called before the first frame update
    void Start()
    {
        sli.maxValue = health;
        direction = new Vector3(
            0,
            Random.Range(-10, 10),
            0
            );
        StartCoroutine(changeDirection());
    }

    // Update is called once per frame
    void Update()
    {
        sli.value = health;
        if(health <= 0)
        {
            Destroy(this.gameObject);
        }
        transform.Rotate(direction);
        Vector3 movement = transform.rotation * Vector3.forward * speed;
        transform.position += movement;
    }
    private void OnCollisionEnter(Collision collision)
    {
        if(collision.gameObject.tag == "PlayerBullet")
        {
            health -= 1;
        }
    }
    //movement
    IEnumerator changeDirection()
    {
        yield return new WaitForSeconds(4f);
        direction = new Vector3(
            0,
            Random.Range(-10, 10),
            0
            );
        StartCoroutine(changeDirection());
    }
}
