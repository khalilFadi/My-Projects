using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class NoiseGenerator : MonoBehaviour
{
    public Texture2D noise;
    public static bool[] cubes;
    public GameObject plane, side;
    public int width, hight;
    public Transform player;
    createCube cubescript;
    // Start is called before the first frame update
    void Start()
    {
        spawnterrain();
    } 
    void spawnterrain() {
        for(int y = 0;y <= width; y+= 2) {
            for(int x = 0; x <= hight; x+= 2)
            {
                
               Debug.Log("instainating ..." + getcolor(y, x));
               Vector3 po = new Vector3(y,getToNearestTwo(40.000f * getcolor(x, y)), x);
                    GameObject g = Instantiate(plane, new Vector3(y, getToNearestTwo(40.000f * getcolor(x, y)), x), transform.rotation);
                g.layer = 8;
                //Vector3 pos = new Vector3(0f, -1f, 1f);
                //GameObject sides = Instantiate(side, g.transform.position + pos, new Quaternion(0f,90f,-90f,0f));
                //sides.transform.SetParent(g.transform);
                //pos = new Vector3(1f, -1f, 0f);
                //sides = Instantiate(side, g.transform.position + pos, new Quaternion(0f, 0f, 0f, 0f));
                //sides.transform.SetParent(g.transform);
                //for the destroying thing at which it check for the number 

            }
        }
    }
    float getcolor(int x, int y)
    {
        Color color = noise.GetPixel(x, y);
        return color.a;
    }
    int getToNearestTwo(float num)
    {
        float output  = Mathf.Round(num);
        int ret = (int)output;
        if(output % 2 != 0)
        {
            output++;
        }
        ret = (int)output;
        return ret;
    }
}
