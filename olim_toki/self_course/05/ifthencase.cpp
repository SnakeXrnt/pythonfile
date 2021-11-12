#include <bits/stdc++.h>
using namespace std;

int main () {
	float angka;
	scanf("%f",&angka);
	if (angka>=1 && angka<10) {
		printf("satuan\n");
	}
	else if (angka<100) {
		printf("puluhan\n");
	}
	else if (angka<1000) {
		printf("ratusan\n");
	}
	else if (angka<10000) {
		printf("ribuan\n");
	}
	else {
		printf("puluhribuan\n");
	}
}