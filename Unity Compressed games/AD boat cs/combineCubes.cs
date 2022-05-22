using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class combineCubes : MonoBehaviour
{
    Vector3 flag;
    public GameObject cube;
    int range = 1;
    public List<Vector3> direction = new List<Vector3>();
    public int dir_num = 0;
    public float size;
    //this will get the mesh filter that we will add the colliders to
    //my plan is something but what?
    /* the solution was to create a for loop that will go 2 cycles
     * the first will add the positive X and y while the other one 
     * will add the negative using the variable NP;
     */
    void Start() {
        cube = transform.Find("Cube1").gameObject;
        size = transform.Find("Cube1").transform.localScale.x;
        Vector3 vec = new Vector3(1, 0, 1);
        //positive is for true while neative is for false
        //it will react with the + and - one
        int NP = -1;
        direction.Add(vec);
        //each 2 loops will create a full circle so this will form 20 circles which is imposible to reach.
        for (int i = 0; i < 40; i++)
        {
            for (int x = 0; x < range * 2; x++)
            {
                vec += new Vector3(0, 0, 1) * NP;
                direction.Add(vec);
            }
            for (int x = 0; x < range * 2; x++)
            {
                vec += new Vector3(1, 0, 0) * NP;
                direction.Add(vec);
            }
            NP *= -1;
            if (i == 1 || i % 3 == 0 && i != 0)
            {
                range += 1;
                vec = new Vector3(range, 0, range);
                direction.Add(vec);
            }
        }
    }
    void Update()
    {
        
    }
    private void OnCollisionEnter(Collision collision)
    {

    }
    public void add_cube(GameObject go)
    {
        flag = transform.position + (direction[dir_num] * size);
        dir_num += 1;
        go.SetActive(false);
        GameObject g = Instantiate(cube, flag, this.transform.rotation);
        g.transform.SetParent(this.transform);
        g.gameObject.tag = "Player";
    }
}
