using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CubeEffects : MonoBehaviour
{
    Rigidbody Rb;
    public float rotationSpeed = 100;
    Vector3 angle;
    // Start is called before the first frame update
    void Start()
    {
        Rb = this.GetComponent<Rigidbody>();
        angle = new Vector3(0, 100, 0);
    }

    // Update is called once per frame
    void Update()
    {
        Quaternion deltaRotation = Quaternion.Euler(angle * Time.deltaTime);
        Rb.MoveRotation(deltaRotation * Rb.rotation);
    }
}
