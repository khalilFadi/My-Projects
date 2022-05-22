#include <iostream>
#include <vector>
#include <string>
#include <iterator>
#include <algorithm>
//print a vector 
void print(std::vector<int> const &input)
{
    std::copy(input.begin(),
            input.end(),
            std::ostream_iterator<int>(std::cout, " "));
}

using namespace std;

vector<int> print_tree(vector<int> vec,int width){
    int x = 0;
    int level = 1;
    for(int i = 0;i < vec.size(); i++){
        float size = width / level;
        cout << string(size, ' ');
        cout << "[" << vec[i] << "](" << i << ")" ;
        x += size;
        if(x >= width){
            x = 0;
            level += 1;
            cout << endl;
        }
    }
    return vec;
}
vector<int> list;
#define loop(i,n, z) for(int i = 0; i < n; i += z)
vector<int> heapsort(int i, vector<int> vec){
    //break if finished 
    if(i < 0){
        return vec;
    }
    //the needed vars
    //head is the element we are working with 
    int head = i;
    //the left and right children 
    int left = (i * 2) + 1;
    int right = (i * 2) + 2;
    //the size of the array to check if there is a right or left element
    //check if left and right exist and swap if less than head
    int size = vec.size();
    if(left < size && vec[left] < vec[head]){
        // print_tree(vec, 20);
        iter_swap(vec.begin() + left, vec.begin() + head);
        vec = heapsort((i - 1) / 2, vec); 
    }
    if(right < size && vec[right] < vec[head]){
        iter_swap(vec.begin() + right, vec.begin() + head);
        vec = heapsort((i - 2) / 2, vec); 
    }
    //to have the smallest one always to the right 
    //although its not that important 
    if(left < size && right < size && right < left){
        iter_swap(vec.begin() + right, vec.begin() + left);
    }
    return vec;
}
//to swap 2 elements
//iter_swap(list.begin() + 0, list.begin() + 2);

//print the current tree
//print_tree(list, 10);
int main()
{   
    int num;
    cin >> num;
    vector<int> result;
    //take the input 
    for(int i = 0;i < num;i++){
        int k;
        cin >> k;
        list.push_back(k);
    }
    //loop until u get it right by accesesing every single least value 
    while(list.size() != 0){
        for(int i = 0;i < num;i++){
            list = heapsort(i, list); 
        }
        result.push_back(list[0]);
        list.erase(list.begin());
    }
    for(int i = 0;i < num;i++){
        cout << result[i] << " ";
    }
}
