#include <bits/stdc++.h>
using namespace std;

int A[105];
int c[105];
int N;

int main() {
	cin >> N;
	
	for (int i = 0; i <= N; i++) {
		int x; cin >> x;
		A[i] = x;
		c[x] >= 0;
		
		if (c[x] == 0){
			cout << "EASY";
		

		}
		else if (c[x] == 1){
			cout << "HARD";
		}
		
	}

}
