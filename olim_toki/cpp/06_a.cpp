#include <bits/stdc++.h>
using namespace std;
/*
int a, sum;

int main() {
	while(cin >> a) {
		sum += a;
		
	}
	cout << sum << "\n";
}
*/
/*
int N;

int main() {
	cin >> N;
	
	while (N % 2 == 0) {
		N /= 2:
	}
	if (N == 1) cout << "ya\n";
	else cout << "bukan\n";
}
*/
/*
int N;

int main() {
	cin >> N;
	
	for (int i = N; i > 0; i--) {
		if (N % i == 0) {
		
			cout << i;
		}
	}
	
}
*/
int N, terbesar, terkecil;

int main() {
	terbesar = -100001;
	terkecil = 100001;
	
	cin >> N;
	
	for (int i = 1; i <= N; i++) {
		int x; cin >> x;
		
		if (x > terbesar) terbesar = x;
		if (x < terkecil) terkecil = x;
		
	}
	cout << terbesar << " " << terkecil << "\n";
}


























