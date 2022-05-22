using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
public class PlayerHealth : MonoBehaviour
{
    public Slider sli;
    public int health = 10;
    // Start is called before the first frame update
    void Start()
    {
        sli.maxValue = health;
    }

    // Update is called once per frame
    void Update()
    {
        sli.value = health;
    }
}
