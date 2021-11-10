#include <bits/stdc++.h>
using namespace std;

int N, T;
int A[1005], B[1005];


void tukar(int &x, int &y) {
	int t = x;
	x = y;
	y = t;	
}


int main () {
	int N; cin >> N;
	for (int i = 1; i <= N; i++) {
		cin >> A[i];
	}
	for (int i = 1; i <= N; i++) {
		cin >> B[i];
	}
	
	cin >> T;
	for (int i = 1; i <= T; i++) {
		char P, Q; int x, y;
		
		cin >> P >> x >> Q >> y;
		
		if (P == 'A' and Q == 'B') {
			tukar(A[x], B[y]);
		}
		else if (P == 'B' and Q == 'A') {
			tukar(B[x], A[y]);
		}
		else if (P == 'A' and Q == 'A') {
			tukar(A[x], A[y]);
		}
		else if (P == 'B' and Q == 'B') {
			tukar(B[x], B[y]);
		}
	}
	
	for (int i = 1; i <= N; i++) {
		cout << A[i];
		if (i < N) cout << " ";
	}
	cout << "\n";
	
	for (int i = 1; i <= N; i++) {
		cout << B[i];
		if (i < N) cout << " ";
	}
	cout << "\n";
}












