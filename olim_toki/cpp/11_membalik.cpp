#include <bits/stdc++.h>
using namespace std;

int A, B, C;
int reverse(int x) {
	int temp = x;
	int ret = 0;
	
	while (temp > 0) {
		ret = (ret * 10) + (temp % 10);
		temp = temp / 10;
	}
	
	return ret;
}


int main () {
	cin >> A >> B;
	
	int a = reverse(A);
	int b = reverse(B);
	C = a + b;
	int ans = reverse(C);
	
	cout << ans << "\n";
}
