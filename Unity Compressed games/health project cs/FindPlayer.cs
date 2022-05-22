using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class FindPlayer : MonoBehaviour
{
    GameObject player;
    public float speed;
    public float backup;
    public float vision;
    public static bool move = true;
    // Start is called before the first frame update
    void Start()
    {
        player = GameObject.Find("player");
    }

    // Update is called once per frame
    void Update()
    {
        float distance = Vector2.Distance(this.gameObject.transform.position, player.transform.position);
        if (move)
        {
            if (distance <= vision) {
                this.gameObject.transform.position = Vector2.MoveTowards(this.gameObject.transform.position, player.transform.position, speed);

            }
        }
    }
    IEnumerator OnCollisionEnter2D(Collision2D collision)
    {
        if(collision.gameObject.tag == "arrow")
        {
            move = false;
            yield return new WaitForSeconds(backup);
            move = true;
        }
    }
}
