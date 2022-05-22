#include <iostream>
#include <fstream>
using namespace std;

int main() {
    fstream myfile;
    myfile.open("input.txt");
    
   string output;
   myfile >> output;
   cout << output;
    return 0;
}