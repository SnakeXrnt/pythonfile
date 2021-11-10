#include <bits/stdc++.h>
using namespace std;

int N;

int main() {
	cin >> N;
	
//	int ans = 0;
	int faktor = 0;
	for (int i = 1; i <= N; i++){
	
		int faktor = 0;
		for (int i = 1; i <= N; i++){
			if (N % i == 0) faktor +=1;
			
			if (faktor >2) break;
		}
	}
		if (faktor == 2) cout << "prima\n";
		else cout << "bukan prima\n";
		
}
