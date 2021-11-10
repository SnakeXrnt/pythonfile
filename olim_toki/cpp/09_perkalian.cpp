#include <bits/stdc++.h>
using namespace std;

int A[105][105], B[105][105], C[105][105];
int N, M, P;

int main() {
	cin >> N >> M;
	
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++){
			cin >> A[i][j];
		}
	}
	
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < P; j++) {
			for (int k = 0; k < M; k++) {
				C[i][j] += (A[i][k] * B[k][j]);
			}
		}
	} 
	
	for (int i = 0; i < M; i++) {
		for (int j = 0; j < P; j ++) {
			cout << C[i][j];
			
			if (j < P - 1) cout << " ";
		}
		
		cout << "\n";
	}
}
