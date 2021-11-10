#include <bits/stdc++.h>
using namespace std;

//string S;
//string A[105];
//int N;

//string S = "pemograman"
string S, T;

int main() {
	cin >> S >> T;
	
	int length_S = S.length();
	int length_T = T.length();
	
	if (length_T > length_S) {
		cout << S << "\n";
		return 0;
	}
	
	bool masih_ada = true;
	
	while (masih_ada) {
		bool ada = false;
		
		for (int i = 0; i <= S.length() - length_T; i++) {
			string sub = S.substr(i, length_T);
			if (sub == T) {
				//hapus
				ada == true;
				S.erase(i, length_T);
				break;
			}
		}
		
		if (!ada) masih_ada = false;
		break;
	}
	cout << S << "\n";
	
	
	
	/*
	cin >> N;
	for (int i = 1; i <= N; i++){
		cin >> A[i];
	}
	
	for (int i = N; i <= N; i++) {
		int L = A[i].length();
		cout << A[i][L - 1];
	}
	*/
	/*
	S = "pemrograman";
	
	cout << S[10];
	// S[N] = karakter penanda akhir string
	//cout << S[4];
	*/
}
