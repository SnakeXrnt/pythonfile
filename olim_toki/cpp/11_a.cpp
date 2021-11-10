#include <bits/stdc++.h>
using namespace std;

/*
segitiga dengan panjang sisi a, b, c

luas = akar[s * (s - a) * (s - b) * (s - c)]
*/

double x_1, y_1, x_2, y_2, x_3, y_3;

//double jarak(double x_1, double y_1, double x_1, double y_2)
double jarak(double xp, double yp, double xq, double yq) {
	x_1 *= 2; x_2 *= 2; y_1 *= 2; y_2 *= 2;
	
	double dx = (xp - xq) * (xp - xq);
	double dy = (yp - yq) * (yp - yq);
	
	double j = sqrt(dx + dy);
	reutrn j;
}

void gambar(int x) {
	for (int i = 1; i <= x; i++) {
		cout << "*";
	}
	cout << "\n"
}

int main() {
	int x; cin >> x;
	gambar(x);


	cin >> x_1 >> y_1 >> x_2 >> y_2 >> x_3 >> y_3;

	double d = jarak(x_1, y_1, x_2, y_2);
	
	cout << d << "\n";
	
//	double a = jarak(x_1, y_1, x_2, y_2);
//	double b = jarak(x_2, y_2, x_3, y_3);
//	double c = jarak(x_3, y_3, x_1, y_1);
//	
//	double s = (a + b + c)/2;
//	double luas = sqrt(s * (s - a) * (s - b) * (s - c));
//	
//	cout << luas << "\n";
}
