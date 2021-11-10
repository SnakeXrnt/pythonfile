#include <bits/stdc++.h>
using namespace std;

int T, N;

int main() {
	cin >> T;
	
	for (int t = 1; t <= T; t++) {
		bool sudah[15];
		for (int t = 0; i < 15; i++){
			sudah[i] = false;
		}
		cin >> N;
		for (int i = 1; i <= N - 1; i++) {
			int x; cin >> x;
			sudah[x] = true;
		}
		for (int i = 1; i <= N; i++) {
			if (not sudah[i]) {
				cout << i << "\n";
				break;
			}
		}
	}
	
}

