using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class choseBlock : MonoBehaviour
{
    public Material color;
    public GameObject test = new GameObject();
    public bool show = true;
    string key;
    // Start is called before the first frame update
    void Start()
    {
        test.AddComponent<BuildTowers>();
    }

    // Update is called once per frame
    void Update()
    {
        RaycastHit hit;
        RaycastHit empty;
        /*this will be used to check if the hit is
        *changed so it changes the last hit to what it
        was before */
        Ray ray = Camera.main.ScreenPointToRay(Input.mousePosition);
        if(Physics.Raycast(ray, out hit, Mathf.Infinity))
        {
            key = "";
            if (hit.transform.gameObject.tag == "Player")
            {
                key = "color";
                hit.transform.gameObject.GetComponent<BuildTowers>().id = key;
                if(test != hit.transform.gameObject)
                {
                    test.gameObject.GetComponent<BuildTowers>().id = "";
                    test = hit.transform.gameObject;
                }
            }
            else
            {
                if(hit.collider == null)
                {
                    test.gameObject.GetComponent<BuildTowers>().id = "";
                }
                key = "";
            }
        }
    }
    /*
     * if ( Input.GetMouseButtonDown (0)){ 
         RaycastHit hit; 
         Ray ray = Camera.main.ScreenPointToRay(Input.mousePosition); 
         if ( Physics.Raycast (ray,out hit,100.0f)){ 
         //suppose i have two objects here named obj1 and obj2.. how do i select obj1 to be transformed 
         if(hit.transform!=null) { 
         transform.Translate (Time.deltaTime, 0, 0, Space.Self); 
         } 
         }
    */
    //this will be responsilbe to showing and hiding the needed block
    public void hide_show()
    {
        show = !show;
    }
}
