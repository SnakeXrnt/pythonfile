#include <bits/stdc++.h>
using namespace std;

int N;
int A[100]; 

int main() {
	cin >> N;
	for (int i = 0; i < N; i++) {
		cin >> A[i];
	}
	
	for (int i = N -1; i>=0; i--) {
		cout << A[i] << " ";
	}
	
}
