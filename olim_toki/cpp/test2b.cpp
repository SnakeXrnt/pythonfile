#include <bits/stdc++.h>
using namespace std;

int T;

int main() {
	cin >> T;
	
	for (int t = 1; t <= T; t++) {
		int N, A, B;
		cin >> N >> A >> B;
		
		string S;
		char c = 'a';
		char karakter_ke_b = 'a' + b - 1;
		for (int i = 1; i <= N; i++) {
			S += c;
			c += 1;
			if (c > karakter_ke_b) c = 'a'
		}
		
		cout << S << "\n"
	}	
}
