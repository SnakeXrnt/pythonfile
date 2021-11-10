#include <bits/stdc++.h>
using namespace std;

int A[100005];
//int f[100005];
int c[105];
int N;

int main() {
	cin >> N;
	
	for (int i = 1; i <= N; i++) {
		int x; cin >> x;
		A[i] = x;
		c[x] += 1;
	}
	int m = 1000000;
	for (int i = 1; i <= N; i++) {
		if (c[A[i]] < m and c[A[i]] > 0)
			m = c[A[i]];
	}
	
	for (int i = 1; i <= N; i++){
		if (c[A[i]] == m) {
			cout << A[i] << " ";
		}
	}
	
	/*
	f[1] = 4; f[2] = -1;
	
	for (int i; i <= N; i++) {
		f[1] = f[i - 1] + f[i - 2];
		//cin >> A[i];
	}
	
	//for (int i = N - 1; i >= 1; i--) {
	//	A[i] = A[N - i];
	//}
	
	for (int i = 1; i <= N; i++){
		cout << f[i] << " ";
	}
	*/
}
