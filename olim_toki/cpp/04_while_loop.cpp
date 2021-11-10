#include <bits/stdc++.h>
using namespace std;

int N; 

int main() {
	cin >> N;
	
	int i = N;
	while (i > 0) {
		i /= 3;
		cout << i <<"\n";
	}
}
