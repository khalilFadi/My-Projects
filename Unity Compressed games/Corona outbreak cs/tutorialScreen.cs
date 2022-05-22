using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class tutorialScreen : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {
        this.gameObject.SetActive(true);
        Time.timeScale = 0f;
    }
    public void hidepanel()
    {
        this.gameObject.SetActive(false);
        Time.timeScale = 1f;
    }
    
}
