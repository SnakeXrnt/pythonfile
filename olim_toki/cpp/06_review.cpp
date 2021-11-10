#include <bits/stdc++.h>
using namespace std;

int N, r;

int main() {
	cin >> N >> r;
	
	int s = 0;
	int p = 1;
	for (int i = 1; i <= N; i++){
		s += p;
		p *= r;
	
	}
	
	
	cout << s << "\n";
}
