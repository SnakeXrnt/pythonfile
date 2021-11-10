#include <bits/stdc++.h>
using namespace std;

int N;

int main() {
	cin >> N;
	
	for (int i = 1; i <= N; i++){
		if (i % 10 == 0) continue;
		
		if(i == 42){
			cout << "ERROR\n";
			break;
		}
		else cout << i << "\n";
	}
}
