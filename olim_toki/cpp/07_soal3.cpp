#include <bits/stdc++.h>
using namespace std;

int N;

int main() {
	cin >> N;


	int banyak_prima = 0;
	int n = 2;
	
	while (banyak_prima < N) {
		int faktor = 0;
		for (int i = 1; i <= N; i++){
			if (N % i == 0) faktor +=1;			
			if (faktor >2) break;
		}
		if (faktor == 2) {
			cout << n << " ";
			banyak_prima += 1;
		}
	}
		
		n += 1;
}
