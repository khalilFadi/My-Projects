using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class createCube : MonoBehaviour
{
    public GameObject plane;
    public Material []MyMaterials;
    public MeshRenderer mymesh;
    public int[] position;
    public int i;
    void Update()
    {
        
    }
    private void Awake()
    {
        //checkeach();
        checkeach();
    }
    void createplane(int side)
    {
        Vector3 roation;
        Vector3 pos;
        switch (side)
        {
            case 1:
                roation = new Vector3(0, 0, 90);
                pos = new Vector3(0, 0.997f, 0);                
                break;
            case 2:
                roation = new Vector3(0, 0, 0);
                pos = new Vector3(0.997f, 0, 0);
                spawnplane(roation, pos);
                break;
            case 3:
                roation = new Vector3(0, 0, 0);
                pos = new Vector3(-0.997f, 0, 0);
                spawnplane(roation, pos);
                break;
            case 4:
                roation = new Vector3(0, 90, 90);
                pos = new Vector3(0, 0, 0.997f);
                break;
            case 5:
                roation = new Vector3(0, 90, 90);
                pos = new Vector3(0, 0, -0.997f);
                break;
            case 6:
                roation = new Vector3(0, 0, 90);
                pos = new Vector3(0, -0.997f, 0);
                break;
            default:
                roation = new Vector3(0, 0, 0);
                pos = new Vector3(0, -0.997f, 0);
                break;
        }
        mymesh.material = MyMaterials[side];
        
        spawnplane(roation, pos);
    }
    void spawnplane(Vector3 rotatio, Vector3 pos)
    {
        GameObject g = Instantiate(plane, pos, plane.transform.rotation);
        g.transform.Rotate(rotatio);
        g.transform.SetParent(this.transform);
    }
    bool checkforcube(int x, int y, int z,int side)
    {
        bool output = false;
        
            createplane(side);
        
        return output;
    }
    void checkeach()
    {
        checkforcube(0, 1, 0, 1);
        checkforcube(1, 0, 0, 2);
        checkforcube(1, 0, 0, 3);
        checkforcube(0, 0, -1, 4);
        checkforcube(0, 0, 1, 5);
    }
}
