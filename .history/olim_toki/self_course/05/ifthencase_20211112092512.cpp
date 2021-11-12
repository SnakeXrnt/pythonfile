#include <bits/stdc++.h>
using namespace std;

int main () {
	float number;
	scanf("%f",&number);
	if (number>=1 && number<10) {
		printf("satuan\n");
	}
	else if (number<100) {
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