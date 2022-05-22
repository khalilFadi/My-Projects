using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CameraMovment : MonoBehaviour
{
    public Vector3 offset;
    public GameObject camera;
    public GameObject player;
    private void LateUpdate()
    {
        camera.transform.position = player.transform.position + offset;
    }
}
