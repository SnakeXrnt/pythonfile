#include <bits/stdc++.h>
using namespace std;

int N;
int A[105]; 
int B[105]; // frekuensi[x] = x muncul berapa kali

int main() {
	// mencatat frekuensi
	cin >> N;
	for (int i = 0; i < N; i++) {
		int x; cin >> x;
		A[i] = x;
		B[x] += 1;
	}
	
	cout <<"\n";
	
}
	
	
	
