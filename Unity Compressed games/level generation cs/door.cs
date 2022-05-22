using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;
public class door : MonoBehaviour
{
    public bool nextlevel;
    public int level;
    private void OnCollisionEnter2D(Collision2D collision)
    {
        if(collision.gameObject.tag == "Player")
        {
            if (nextlevel)
            {
                int name = SceneManager.GetActiveScene().buildIndex;
                Debug.Log("next scene " + (name + 1));
                SceneManager.LoadScene(name + 1);
            }
            else
            {
                SceneManager.LoadScene(level);
            }
        }
    }

}
