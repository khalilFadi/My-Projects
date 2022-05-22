using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.Networking;
public class BulletSpawner : NetworkBehaviour
{
    public int x, y;
    public GameObject bullet;
    // Start is called before the first frame update
    void Start()
    {
        if (isServer == true){
            bulletspawner();
        }
        
    }

    // Update is called once per frame
    void Update()
    {
        
    }
    void bulletspawner()
    {
        for(float i = 0;i < x; i += 0.2f)
        {
            for(float o = 0;o < y; o += 0.2f)
            {
                Vector3 position = new Vector3(transform.position.x + i,transform.position.y +  o, 0);
                GameObject g = Instantiate(bullet, position,transform.rotation);
                NetworkServer.Spawn(g);
            }
        }
    }
}
