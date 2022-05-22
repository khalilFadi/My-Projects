using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlayerMovment : MonoBehaviour
{
    public Rigidbody RB;
    public Camera camera;
    public int speed;
    public GameObject Cube;
    public int RotationSpeed;
    public int jumphigh;
    bool jump = true;
    // Start is called before the first frame update
    void Start()
    {
        RB = this.GetComponent<Rigidbody>();
    }


    void Update()
    {
        movement();
        if (Input.GetMouseButtonDown(0))
        {
            DestroyCubes();
        }
    }

    void movement()
    {
        if (Input.GetKey(KeyCode.W))
        {
            transform.position += transform.forward * speed * Time.deltaTime;
        }
        else if (Input.GetKey(KeyCode.S))
        {
            transform.position += transform.forward * speed * Time.deltaTime * -1;
        }
        if (Input.GetKey(KeyCode.A))
        {
            transform.position += transform.right * speed * Time.deltaTime * -1;
        }
        else if (Input.GetKey(KeyCode.D))
        {
            transform.position += transform.right * speed * Time.deltaTime;
        }
        if (Input.GetKeyDown(KeyCode.Space))
        {
            if (jump)
            {
                StartCoroutine(jumping());
            }
        }
    }
    IEnumerator jumping()
    {
        for (int i = 0; i < 10; i++)
        {
            yield return new WaitForSeconds(0.01f);
            transform.position += transform.up * (jumphigh / 10) * Time.deltaTime;
        }
    }

    //destroy objects when cliked on them
    void DestroyCubes()
    {
        RaycastHit hit;
        Ray ray = camera.ScreenPointToRay(Input.mousePosition);
        if (Physics.Raycast(ray, out hit))
        {
            Transform objectHit = hit.transform;
            if (objectHit.gameObject.layer == 8)
            {
                //i need to check all teh direction to c if i need to build somewhere else
                Vector3 pos = new Vector3(0f, -2f, 0f);
                GameObject obj = objectHit.parent.transform.gameObject;
                Debug.DrawRay(objectHit.transform.position + new Vector3(2, -2, 0), Vector3.left, Color.red, 100);
                RaycastHit checkobject;
                if(Physics.Raycast(objectHit.transform.position + new Vector3(2,-2,0) , Vector3.left, out checkobject))
                {
                   
                        
                    
                }
                if (checkobject.transform.gameObject == null) {
                    Instantiate(Cube, objectHit.transform.position + new Vector3(2, -2, 0), new Quaternion(0, 0, 0, 0));
                }
                Destroy(objectHit.parent.transform.gameObject);
                Instantiate(Cube, obj.transform.position + pos, new Quaternion(0, 0, 0, 0));
                RaycastHit left;
                
                //pos = new Vector3(2f, -2f, 0f);
                //Instantiate(Cube, obj.transform.position + pos, new Quaternion(0, 0, 0, 0));
                //pos = new Vector3(-2f, -2f, 0f);
                //Instantiate(Cube, obj.transform.position + pos, new Quaternion(0, 0, 0, 0));
                //pos = new Vector3(0f, -2f, 2f);
                //Instantiate(Cube, obj.transform.position + pos, new Quaternion(0, 0, 0, 0));
                //pos = new Vector3(0f, -2f, -2f);
                //Instantiate(Cube, obj.transform.position + pos, new Quaternion(0, 0, 0, 0));
                //if (Physics.Raycast(obj.transform.position, Vector3.left, out left, 1f))
                //{
                //    if(left.transform.gameObject != null)
                //    {
                //        pos = new Vector3(2f, -2f, 0f);
                //        //Instantiate(Cube, obj.transform.position + pos, new Quaternion(0, 0, 0, 0));
                //        //pos = new Vector3(-2f, -2f, 0f);
                //        //Instantiate(Cube, obj.transform.position + pos, new Quaternion(0, 0, 0, 0));
                //        //pos = new Vector3(0f, -2f, 2f);
                //        //Instantiate(Cube, obj.transform.position + pos, new Quaternion(0, 0, 0, 0));
                //        //pos = new Vector3(0f, -2f, -2f);
                //        //Instantiate(Cube, obj.transform.position + pos, new Quaternion(0, 0, 0, 0));
                //    }
                //}
            }
            
        }

    }

}

