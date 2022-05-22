using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class chossebuilding : MonoBehaviour
{
    public string type;
    public GameObject player;
    public GameObject house;
    Vector3 offset = new Vector3(0, 3, 0);
    public Material transparent;
    Material original;
    GameObject canvas;
    // Start is called before the first frame update
    void Start()
    {
        canvas = GameObject.Find("Canvas");
        original = house.GetComponent<Renderer>().material;
        house.GetComponent<Renderer>().material = transparent;
        player = GameObject.Find("Player");
    }

    // Update is called once per frame
    void Update()
    {
        type = this.gameObject.GetComponent<BuildTowers>().id;
        if(type == "color")
        {
            house.transform.position = this.transform.position+ offset;
        }
        house.SetActive(canvas.GetComponent<choseBlock>().show);
    }
    private void OnMouseDown()
    {
        GameObject g = Instantiate(house, this.transform.position + offset, this.transform.rotation);
        g.GetComponent<Renderer>().material = original;
        g.GetComponent<Collider>().isTrigger = false;
        Rigidbody RB = g.AddComponent<Rigidbody>();
        g.transform.SetParent(player.transform);
        //StartCoroutine(timer(RB));
        RB.constraints = RigidbodyConstraints.FreezePositionZ | RigidbodyConstraints.FreezePositionX;
    }
    IEnumerator timer(Rigidbody RB)
    {
        yield return new WaitForSeconds(1f);
        RB.constraints = RigidbodyConstraints.FreezeAll;
        RB.isKinematic = true;
        RB.useGravity = false;
    }
}
