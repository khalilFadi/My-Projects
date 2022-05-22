#include <iostream>
#include <vector>
using namespace std;
int n;
vector<int> haircutter;
int check_for_empty(){
    for(int i = 0;i < haircutter.size();i++){
        if(haircutter[i] == 0){
            return i;
        }
    }
    return -1;
}
int main() {
    int n, x;
    cin >> n >> x;
    vector<int> haircutter_time;
    for(int i = 0;i < n;i++){
        int k;
        cin >> k;
        haircutter_time.push_back(k);
        haircutter.push_back(0);
    }
    int customers = x;
    int minute = 0;
    while(x >= customers){
        if(check_for_empty() != -1){
            haircutter[check_for_empty()] = haircutter_time[check_for_empty()];
            customers--;
        }
        minute++;
        if(customers >= 0){
            break;
        }
    }
    cout << minute;
    //first i need to save the number of hair cutters 
    //ill create a for loop for each minute 
    //then each hair cutter will take one each turn he is 0
    //when we find the vector is empty and any of the haircutter are free
    //we will output the minute 

}
