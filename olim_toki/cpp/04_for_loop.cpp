#include <bits/stdc++.h>
using namespace std;

int N; // global variable

int main() {
	cin >> N;
	
	long long s = 1;
	
	for (int i = 1; i <= N; i +=1) {
		// i -> local variable
		s = s * 2;
	}
	
	cout << s << "\n";
	
}
