#include <bits/stdc++.h>
using namespace std;

int N;
int A[110]; 

int main() {
	int x;
	int indeks = 0;
	
	while (cin >> x) {
		A[indeks] = x;
		indeks += 1;
	}
	
	for (int i = indeks -1; i >= 0; i--){
		cout << A[i] << "\n";
	}
	
}
