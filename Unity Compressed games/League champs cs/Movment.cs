using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Movment : MonoBehaviour
{
    Vector3 position;
    public float speed;
    float y;
    // Start is called before the first frame update
    void Start()
    {
        position = this.transform.position;
        y = position.y;
    }

    // Update is called once per frame
    void Update()
    {
        RaycastHit hit;
        Ray r = Camera.main.ScreenPointToRay(Input.mousePosition);
        if(Physics.Raycast(r, out hit, Mathf.Infinity) && Input.GetMouseButtonDown(1))
        {
            if(hit.transform.gameObject.tag == "ground")
            {
                position = hit.point;
                position.y = y;
            } 
        }
        this.transform.position = Vector3.MoveTowards(this.transform.position, position, speed);
    }
}
