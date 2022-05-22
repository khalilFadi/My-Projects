using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class playerSounds : MonoBehaviour
{
    public GameObject bumb;
    private void OnCollisionEnter2D(Collision2D collision)
    {
        if (collision.gameObject.tag == "wall")
        {
            GameObject gam = Instantiate(bumb);
            destroy(gam);
        }
    }
    IEnumerator destroy(GameObject gam)
    {
        yield return new WaitForSeconds(1f);
        destroy(gam);
    }
}
