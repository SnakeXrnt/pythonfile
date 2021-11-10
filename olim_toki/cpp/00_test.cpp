#include <bits/stdc++.h>
using namespace std;

int n ,m, a , b ;

int main() {
    cin >> n >> m;

    a = n / m;
    b = n % m;

    cout << "masing-masing " << a << "\n";
    cout << "sisa " << b;
}
