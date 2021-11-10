#include <bits/stdc++.h>
using namespace std;

int N, M;

int main() {
	cin >> N >> M;
	
	// kalo N baris, 1 kolom
	for (int i = 1; i <= N; i++){
		for (int j = 1; j <= M; j++){
			cout << "*";
		}
		
		cout << "\n";
	}
}
