using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;
public class Canva : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {
        this.gameObject.SetActive(false);
    }

    // Update is called once per frame
    void Update()
    {
        if (Input.GetKeyDown(KeyCode.Escape))
        {
            this.gameObject.SetActive(true);
            Debug.Log("esc is clicked");
        }
    }
    public void sceen(int scenenum)
    {
        Time.timeScale = 1f;
        
        SceneManager.LoadScene(scenenum);
    }
    
}
