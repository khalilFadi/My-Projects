using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class plantScript : MonoBehaviour
{
    public float distance;
    public GameObject finished;
    // Start is called before the first frame update
    void Start()
    {
        
    }
    private void Awake()
    {
        StartCoroutine(moveup());
    }

    
    IEnumerator moveup()
    {
        for (int i = 0; i < distance; i++)
        {
            
                yield return new WaitForSeconds(0.1f);
                transform.Translate(0, 0.1f, 0);
        }
        finished.SetActive(true);
    }
}
