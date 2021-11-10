#include <bits/stdc++.h>
using namespace std;

int N;
int A[100005]; 
int frekuensi[1005]; // frekuensi[x] = x muncul berapa kali

int main() {
	// mencatat frekuensi
	cin >> N;
	for (int i = 0; i < N; i++) {
		int x; cin >> x;
		A[i] = x;
		frekuensi[x] += 1;
	}
	//cari frekuensi terbesar
	int frekuensi_terbesar = -1;
	for (int i = 0; i <= 1000; i++){
		if (frekuensi[i] > frekuensi_terbesar)
			frekuensi_terbesar = frekuensi[i];
	}
	
	// cari modus terbesar 
	int modus = -1;
	for (int i = 0; i < N; i++) {
		if (frekuensi[A[i]] == frekuensi_terbesar){
			if (A[i] > modus)
				modus = A[i];
		}
	}
	
	cout << modus <<"\n";
	
	
	//for (int i = 1; i <= 10; i++) {
	//	cout << i << "muncul" << frekuensi[i] << "kali\n";
	//}
	
}
