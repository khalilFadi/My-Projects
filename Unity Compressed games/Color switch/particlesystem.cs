using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class particlesystem : MonoBehaviour
{
    public Renderer effects;
    public Renderer player;

    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        effects.material = player.material;
    }

    
}
