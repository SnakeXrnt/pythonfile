#include <bits/stdc++.h>
using namespace std;

int A, B, K, x;

int f(int A, int B, int x) {
	return abs(A * x + B);
}

int main() {
	cin >> A >> B >> K >> x;
	
	int hasil = x;
	for (int i = 1; i <= K; i++) {
		hasil = f(A, B, hasil);
	}
	
	cout << hasil << "\n";
}

/*
f(x) = |x + 1|
f(1) = 2

3 -1 5 0
f(x) = |3x - 1|

f(0) = 1
f(f(0)) = f(1) = 2
f(f(f(
*/
