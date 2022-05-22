#include <iostream>
#include <vector>
#include <string>
#include <iterator>
//print a vector 
void print(std::vector<int> const &input)
{
    std::copy(input.begin(),
            input.end(),
            std::ostream_iterator<int>(std::cout, " "));
}
using namespace std;

vector<int> list;
int main()
{   
    string num;
    cin >> num;
    cout << num;
}
