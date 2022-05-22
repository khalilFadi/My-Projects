using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class camerMovement : MonoBehaviour
{
    Vector3 cameraT;
    Transform player;
    float cooldownTime = 0.5f;
    public GameObject[] Player;
    public int playersize;
    int rotationD;
    // Start is called before the first frame update
    void Start()
    {
        cameraT = this.GetComponent<Transform>().position;
        player = GameObject.Find("Player").transform;
    }

    // Update is called once per frame
    void Update()
    {
        StartCoroutine(movet(player.position));
        Player = GameObject.FindGameObjectsWithTag("Player");
        playersize = Player.Length;
    }
    IEnumerator movet(Vector3 pos)
    {
        yield return new WaitForSeconds(cooldownTime);
        Vector3 offset  = cameraT + new Vector3(0, playersize, -playersize);
        this.transform.position = pos + offset;
        float amount = 1;
        if(rotationD < playersize && playersize < 10){
            this.transform.Rotate(amount,0,0);
            amount /= 2;
            rotationD += 1;
        }
    }

}
