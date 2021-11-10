#include <bits/stdc++.h>
using namespace std;

int N, M;
int a,b;

int main() {
	cin >> N;
	cin >> M;
	a = N / M;
	b = N % M;
	cout << "masing-masing " << a <<"\n";
	cout << "bersisa " << b << "\n";
}
