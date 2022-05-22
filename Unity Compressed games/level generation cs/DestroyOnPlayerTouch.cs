using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class DestroyOnPlayerTouch : MonoBehaviour
{
    public GameObject particleeffects;
    public GameObject destroying;
    public string name;
    private void OnCollisionEnter2D(Collision2D collision)
    {
        if (collision.gameObject.tag == name)
        {
            Instantiate(particleeffects, transform.position, transform.rotation);
            if (destroying == null)
            {
                Destroy(this.gameObject);
            }
            else
            {
                Destroy(destroying);
            }
        }
    }

}
