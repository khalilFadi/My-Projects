#include <iostream>
#include <fstream>
#include <vector>
#include <stdlib.h>
#include<stdio.h>
#include<stdlib.h>
using namespace std;


int N;
int main()
{
    cin >> N;
    for(int i = 0;i < N;i++){
        int k;
        bool cont = true, trying = true;
        
        cin >> k;
        for(int i = 0;cont;i++){
            if(k == 1){
                cout << i << endl;
                break;
            }else if(k % 6 == 0){
                    k /= 6;
                trying = true;
            }else if(trying){
                k *= 2;
                    trying = false;
        
            }else{
                if(!trying){
                    cout << -1 << endl;
                    break;
                }
            }
            
        }
    }
}
