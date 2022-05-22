using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.Networking;
public class PlayerClient : NetworkBehaviour
{
    public GameObject playerObj;
    // Start is called before the first frame update
    void Start()
    {
        if(hasAuthority == false)
        {
            return;
        }
        CmdSpawnPlayer();
        Debug.Log("just spawned a new object");
    }

    // Update is called once per frame
    void Update()
    {
        
    }
    GameObject localplayerobj;
    [Command]
    void CmdSpawnPlayer()
    {
        GameObject g = Instantiate(playerObj);
        localplayerobj = g;
        NetworkServer.SpawnWithClientAuthority(g, connectionToClient);
    }
}
