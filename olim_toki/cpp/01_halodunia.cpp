#include <bits/stdc++.h>
using namespace std;

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
