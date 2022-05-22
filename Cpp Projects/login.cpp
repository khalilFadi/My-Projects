#include<cstdio>
#include<cstring>
#include<algorithm>
#include<iostream>
 
using namespace std;
int a[105][105];
int main() {
	int n,k;
	cin>>n>>k;
	for(int t=0; t<n; t++) {
		for(int j=0; j<n; j++) {
			if(t==j) {
				a[t][j]=k;
			}
		}
	}
	for(int t=0; t<n; t++) {
		for(int j=0; j<n; j++) {
			cout<<a[t][j]<<" ";
		}
		cout<<endl;
 
	}
	return 0;
}