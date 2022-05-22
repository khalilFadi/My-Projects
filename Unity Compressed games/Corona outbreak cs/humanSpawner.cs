using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.SceneManagement;
public class humanSpawner : MonoBehaviour
{
    public float time;
    public int MaxX, MaxY, MinX, MinY;
    public GameObject human;
    public GameObject menu;
    public GameObject disease;
    public int density;
    public static int saved;
 
    // Start is called before the first frame update
    void Start()
    {
        
        StartCoroutine(spawner());
        Vector2 position = destination();
        Instantiate(disease, position, this.gameObject.transform.rotation);
        
    }

    // Update is called once per frame
    void Update()
    {
        StartCoroutine(showmenu());
        
    }
    Vector2 destination()
    {
        int randomX = Random.Range(MaxX, MinX);
        int randomY = Random.Range(MaxY, MinY);
        Vector2 destination;
        return destination = new Vector2(randomX, randomY);
    }
    IEnumerator spawner()
    {
        for (int i = density; i > 0; i--) {
            Vector2 position = destination();
        Instantiate(human, position, this.gameObject.transform.rotation);
            yield return new WaitForSeconds(time);
            
         }
    }
    IEnumerator showmenu()
    {
        
        yield return new WaitForSeconds(1f);
        if (saved == 0)
        {
            menu.SetActive(true);
            Time.timeScale = 0f;
        }
        //if (saved == (density * -1))
        //{
        //    SceneManager.LoadScene(0);
        //    Debug.Log("we are here");
        //}
        Debug.Log("saved : " + saved);
        Debug.Log("density: " + density);
    }
    public void nextscene()
    {
        Time.timeScale = 1f;
        Scene scene = SceneManager.GetActiveScene();
        SceneManager.LoadScene(scene.buildIndex + 1);
    }
    //show the time left
    
}
