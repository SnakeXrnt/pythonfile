#include <bits/stdc++.h>
using namespace std;

int T, N;

int main() {
	cin >> N;
	
	for (int i = 1; i <= N; i++){
		int x; cin >> x;
		
		if (x == 1) {
			sulit = true;
			break;
		}
		
	}
	if (sulit) cout << "HARD\n";
	else cout << "EASY\n";
}	
