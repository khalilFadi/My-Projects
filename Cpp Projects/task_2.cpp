#include <iostream>
#include <vector> 
#include <array>
#include <algorithm>
#include<bits/stdc++.h>
using namespace std;
int N;
vector<int> vec;
vector<int> find_smallest(vector<int> vecto){
    vector<int> output;
    int length = vecto.size();
    for(int i = 0;i < length;i++){
        int smallest = vecto[i];
        int position = i;
            for(int x = i;x < length;x++){
                if(vecto[x] < smallest){
                    smallest = vecto[x];
                    position = x;
                }
            }
        vecto.erase(position);
        cout << i << ":i position: " << position << endl;
        output.push_back(smallest);
    }
    return vecto;
}
int main() {
    cin >> N;
    for(int i = 0;i < N;i++){
        int k;
        cin >> k;
        vec.push_back(k);
    }
    vec = find_smallest(vec);
    for(int i = 0;i < N;i++){
        cout << vec[i];
    }
    return 0;
}   
