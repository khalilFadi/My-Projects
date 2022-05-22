using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class buletCode : MonoBehaviour
{
    Vector3 rotation;
    public GameObject Residents,explosion;
    public float speed;
    // Start is called before the first frame update
    void Start()
    {
        
    }
    private void Awake()
    {
        StartCoroutine(leftArea());
    }
    // Update is called once per frame
    void Update()
    {
        Vector3 movement = transform.rotation * Vector3.forward * speed;
        float rateOfScaleDecrease = 0.1f;
        transform.localScale -= new Vector3(rateOfScaleDecrease, rateOfScaleDecrease, rateOfScaleDecrease);
        transform.position += movement;
    }
    private void OnCollisionEnter(Collision collision)
    {
        //8 is for walls 
        if (collision.gameObject.layer == 8 || collision.gameObject.layer == 10)
        {
            this.GetComponent<CapsuleCollider>().radius = 1;
            GameObject g = Instantiate(Residents, transform.position, Residents.transform.rotation);
            Instantiate(explosion, this.transform.position, transform.rotation);
            Destroy(this.gameObject);
            speed = 0;
        }
    }
    IEnumerator leftArea()
    {
        yield return new WaitForSeconds(0.8f);
        GameObject g  = Instantiate(Residents, transform.position, Residents.transform.rotation);
        Instantiate(explosion, this.transform.position,transform.rotation);
        Destroy(this.gameObject);
    }
}
