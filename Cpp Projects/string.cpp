#include <iostream>
#include <algorithm>

using namespace std;
string inp;
string check_change(int pos){
    string original = inp;
    swap(inp[pos],inp[0]);
        for(int i = 1;i < inp.length();i++){
            swap(inp[0],inp[i]);
            cout << inp << endl;
            inp = original;
            swap(inp[pos],inp[0]);
        }
    if(pos + 1 == inp.length()){
        return "1";
    }else{
        return check_change(pos + 1);
    }
}
int main(){
    cin >> inp;
    check_change(0);
}