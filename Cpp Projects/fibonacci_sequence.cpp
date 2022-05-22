#include <iostream>
#include <vector>
using namespace std;
int length = 3000;
int fibonacci_sequence(int x, int m){
    if (x < length){
        cout << x << endl;
        return fibonacci_sequence(m, x + m);
    }else
    {
        return 1;
    }
}
int main(){
    cin >> length;
    fibonacci_sequence(1, 1);
    return 0;
}