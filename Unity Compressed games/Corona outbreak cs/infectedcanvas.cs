using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class infectedcanvas : MonoBehaviour
{
    public GameObject canva;
    public Text timeleft;
    public int timeleftnum;
    
    //show the time left to change back
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        timeleft.text = timeleftnum.ToString();
    }
    IEnumerator timer()
    {
        while (true)
        {
            for(int i = 0;i < 10; i++)
            {
                yield return new WaitForSeconds(1f);
                timeleftnum--;
            }
        }
    }
    
}
