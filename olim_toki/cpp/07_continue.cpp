#include <bits/stdc++.h>
using namespace std;

int N, M;

int main() {
	cin >> N >> M;
	
	for (int i = 1; i <= N; i++){
		if (i % M == 0) continue;
		cout << i << "\n";
		
	}
	cout << "selesai\n";
}
