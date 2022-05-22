using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
public class spawngel : MonoBehaviour
{
    public string click;
    public GameObject weapon;
    GameObject gel;
    public int refiltime;
    public int refiling;
    public Slider refilshowslider;
    bool refilled = true;
    public 
    // Start is called before the first frame update
    void Start()
    {
        refilshowslider.maxValue = refiltime;
        refiling = refiltime;
    }

    // Update is called once per frame
    void Update()
    {
        if (Input.GetKey(click) && refilled)
        {
            Vector3 mousepos = new Vector3(Camera.main.ScreenToWorldPoint(Input.mousePosition).x, Camera.main.ScreenToWorldPoint(Input.mousePosition).y,0);
            gel = Instantiate(weapon,mousepos, this.gameObject.transform.rotation);
            StartCoroutine(destroy());
            refiling = 0;
            refilled = false;
            StartCoroutine(refil());
        }
        refilshowslider.value = refiling;
    }
    IEnumerator refil()
    {
        while (true)
        {
            for (int i = 0; i < refiltime; i++)
            {
                yield return new WaitForSeconds(1f);
                refiling++;
            }
            break;
        }
        refilled = true;
    }
    IEnumerator destroy()
    {
        yield return new WaitForSeconds(5f);
        Destroy(gel);
    }
}
