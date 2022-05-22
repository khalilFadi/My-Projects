using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Generatelevel : MonoBehaviour
{
    public Texture2D map;
    public int num = 0;
    public GameObject background;
    public ColorToPrefab[] objects;
    // Start is called before the first frame update
    void Start()
    {
        generatemylevel();
    }

    // Update is called once per frame
    void Update()
    {
        
    }
    public void generatemylevel()
    {
        for(int x = 0;x < map.width; x++)
        {
            for(int y = 0;y < map.height; y++)
            {
                GenerateTile(x,y);
            }
        }
    }
    void GenerateTile(int x, int y)
    {
        Color col = map.GetPixel(x, y);
        if(col.a == 0)
        {
            
            return; 
        }
        foreach(ColorToPrefab obj in objects)
        {
            if (obj.color.Equals(col))
            {
               GameObject g = Instantiate(obj.prefab, new Vector2(x,y), transform.rotation);
                g.transform.SetParent(background.transform);
            }
        }
    }
}
