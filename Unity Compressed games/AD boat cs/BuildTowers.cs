using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class BuildTowers : MonoBehaviour
{
    public string id;
    public Material originalColor;
    // Start is called before the first frame update
    void Start()
    {
        originalColor = this.gameObject.GetComponent<MeshRenderer>().material;
    }
    private void Awake()
    {
        id = "";
    }
    // Update is called once per frame
    void Update()
    {
        if(id == "color")
        {
            this.gameObject.GetComponent<MeshRenderer>().material.color = Color.yellow;
        }
        if(id == "")
        {
            this.gameObject.GetComponent<MeshRenderer>().material.color = Color.black;
        }
    }
}
