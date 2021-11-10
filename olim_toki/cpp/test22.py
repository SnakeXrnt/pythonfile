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
}
