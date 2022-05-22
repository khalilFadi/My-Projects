#include <iostream>
#include <vector>
using namespace std;
#define N 5
int graph[N][N];
vector<int> positions[8];
int len = 0;
int output = 0;
int rows = 0;
bool check_collision(int map[][N],int x1, int y1){
    bool output = false;
    for (int i = 0; i < N; i++){
		if (map[x1][i] == 1){
			return true;
        }
    }
    for(int x = x1, y = y1; x >= 0 && y >= 0;x--,y--){
        if(map[x][y] == 1){
            return true;
        }
    }
    for(int x = x1, y = y1; x >= 0 && y >= 0;x--,y++){
        if(map[x][y] == 1){
            return true;
        }
    }

    for(int x = x1, y = y1; x >= 0 && y >= 0;x++,y++){
        if(map[x][y] == 1){
            return true;
        }
    }
    return false;
}
int main(){
    int num1, num2;
    cin >> len >> num1 >> num2;
    for(int i = 0;i < len;i++){
        for(int x = 0;x < len;x++){
            graph[i][x] = 0;
        }
    }
    graph[0][0] = 1;
    cout << check_collision(graph,num1, num2) << endl;
    for(int i = 0;i < len;i++){
        for(int x = 0;x < len;x++){
            cout << graph[i][x];
        }
        cout << endl;
    }
    return 0;
}
