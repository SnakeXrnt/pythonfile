#include <bits/stdc++.h>
using namespace std;

int N , M , a , b ;

int main() {
    cin >> N >> M ;
    a = N / M ;
    b = N%M ;

    cout << "masing-masing " << a << "\n";
    cout << "sisa " << b;
}
