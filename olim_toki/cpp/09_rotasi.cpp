#include <bits/stdc++.h>
using namespace std;

int A[105][105], B[105][105];
int N, M;

int main() {
	cin >> N >> M;
	
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++){
			cin >> A[i][j];
		}
	}
	
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			B[j][N - 1 - i] = A[i][j];
		}
	} 
	
	for (int i = 0; i < M; i++) {
		for (int j = 0; j < N; j ++) {
			cout << B[i][j];
			
			if (j < N - 1) cout << " ";
		}
		
		cout << "\n";
	}
}
