#include <bits/stdc++.h>
using namespace std;

int A, B;
int jumlah_dua_kali(int &x, int &y) {
	x *= 2; y *= 2;
	int C = x + y;
	return C;

}

void tukar(int &x, int &y) {
	int t = x;
	x = y;
	y = t;
}


int main () {
	cin >> A >> B;
	tukar(A, B);
	cout << A << " " << B << "\n";
}
