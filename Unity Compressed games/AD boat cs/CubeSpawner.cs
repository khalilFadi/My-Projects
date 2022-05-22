using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CubeSpawner : MonoBehaviour
{
    public int number;
    public Vector2Int mapMax;
    public Vector2Int mapMin;
    public GameObject Cube;
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        number -= 1;
        if(number > 0)
        {
            int x = Random.Range(mapMin[0], mapMax[0]);
            int z = Random.Range(mapMin[1], mapMax[1]);
            Instantiate(Cube, new Vector3(x, 0, z), Quaternion.identity);

        }
    }
}
