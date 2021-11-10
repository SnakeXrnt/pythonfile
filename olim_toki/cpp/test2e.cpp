#include <bits/stdc++.h>
using namespace std;

int T, N;

int main() {
	cin >> T;
	
	for (int t = 1; t <= T; t++) {
		int K, P, N;
		cin >> K >> P >> N;
		
		if (K > P) {
			cout << (K - P) * N << "\n";
		}
		else {
			cout << "0\n";
		}
	}
}
