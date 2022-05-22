using System.Collections;
using System.Collections.Generic;
using UnityEngine;

//this code defines karma's Q
//the goal iis to move in the position of the cursor when q is clicked and explode if it hits something
//other than that it'll disappear 

public class bullet : MonoBehaviour
{
    public GameObject QObject;
    public GameObject goal;
    GameObject g;
    // Start is called before the first frame update
    void Start()
    {
        
    }
    private void Awake()
    {

    }
    // Update is called once per frame
    void Update()
    {
        if (Input.GetKeyDown(KeyCode.Q))
        {
            g = Instantiate(QObject, goal.transform.position, this.transform.rotation);
        }
        //g.transform.position = Vector3.forward * Time.deltaTime * speed;
    }
}
