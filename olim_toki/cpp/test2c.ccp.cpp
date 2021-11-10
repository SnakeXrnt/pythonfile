#include <bits/stdc++.h>
using namespace std;

int T;

int main() {
	cin >> T;
	
	for (int t = 1; t <= T; t++) {
		int A[105], N, frek[105];
		
		for (int i = 0; i < 105; i++) {
			frek[i] = 0;
		}
		cin >> N;
		
		for (int i = 1; i <= N; i++) {
			cin >> A[i];
			frek[A[i]] +=1;
		}
		int mA = 200;
		for (int i = 0; i <= 100; i++) {
			if (frek[i] == 0) {
				mA = i; break;
			}
		}
		int mB = mA;
		for (int i = 0; i <= mA; i++) {
			if (frek[i] == 1) {
				mB = i; break;
			}
		}
		cout << mA + mB << "\n";
		
	}
}
