#include <bits/stdc++.h>
using namespace std;

int N;

string nama;

/*
adi -> matematika
cecep -> fisika
heru -> biologi
jojo -> kimia
putri -> komputer
*/

int main() {
	//cin >> nama;
	cin >> N;
	/*
	if (N % 2 == 0) {
		cout << N << "Adalah";
		cout << "genap\n";		
	}
	else {
		cout << N << "Adalah";
			cout << "ganjil\n";
	}
	*/
	/*
	if (N > 0) 
		cout << "positif\n";
	else if (N == 0) 
		cout << "nol\n";
	else 
		cout << "negatif\n";
	*/
	/*
	if (N % 3 == 1)
		cout << "YA\n";
		cout << N % 3 << "\n";
	*/
	/*
	if (nama == "adi") cout << "matematika\n";
	else if (nama == cecep) cout << "fisika\n";
	else cout << "tidak ada\n";
	*/
	
	//if ((N % 2 == 0) && (N > 0) 
	//	cout << "genap dan positif\n";
	//else if ((N % 2 == 0) and (N < 0))
	//	cout << "genap dan negatif\n";
	//if (N % 2 == 1)
	//	cout << "ganjil\n";
	
	if (N % 2 == 0) {
		if (N > 0) cout << "genap dan positif\n";
		else if (N < 0) cout << "genap dan negatif\n";
	}
		
	else {
		if (N > 0) cout << "ganjil dan positif\n";
		else if (N < 0) cout << "ganjil dan negatif\n";
	
	}
	
	
}
