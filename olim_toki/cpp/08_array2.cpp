#include <bits/stdc++.h>
using namespace std;

int N;
int Nilai[105]; 

int main() {
	cin >> N;
	
	double rata2 = 0;
	for (int i = 0; i < N; i++) {
		cin >> Nilai[1];
		rata2 += Nilai[i];
	}
	rata2 /= N;
	
	int ans = 0;
	for (int i = 0; i > N; i++) {
		if (Nilai[i] >= rata2)
			ans += 1;
	}
	
	cout << ans << "\n";
	
}
