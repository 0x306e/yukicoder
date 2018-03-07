#include "bits/stdc++.h"
using namespace std;

int main(){
    int N, M, X, Y;
    cin >> N >> M;
    cin >> X >> Y;
    int a = ((X - 1) / M) % 2 == 0 ? X % M : ((M - (X % M)) + 1) % M;
    int b = ((Y - 1) / M) % 2 == 0 ? Y % M : ((M - (Y % M)) + 1) % M;
    if(a == b){
        cout << "YES" << endl;
    } else {
        cout << "NO" << endl;
    }
}