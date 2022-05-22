using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class NoiseGenerator1 : MonoBehaviour
{
    public Texture2D noise;
    public static bool[] cubes;
    public GameObject cube;
    public int width, hight;
    createCube cubescript;
    // Start is called before the first frame update
    void Start()
    {
        spawnterrain();
    }
    void spawnterrain() {
        for(int y = 0;y <= width; y += 2) {
            for(int x = 0;x <= hight; x += 2)
            {
                
               Debug.Log("instainating ..." + getcolor(y, x));
               Vector3 po = new Vector3(y,getToNearestTwo(40.000f * getcolor(x, y)), x);
                for (int i = 0; i <= getToNearestTwo(40.000f * getcolor(x, y)); i += 2)
                {
                    
                    GameObject g = Instantiate(cube, new Vector3(y, i, x), transform.rotation);
                    //for the destroying thing at which it check for the number 
                    g.layer = 8;
                }
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
        return ret;
    }
}
