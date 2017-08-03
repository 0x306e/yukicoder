#include <iostream>
#include <string>
using namespace std;

int main(void) {
    int N;
    string S[11], T[11];
    cin >> N;
    for(int i = 0; i < N; i++) {
        cin >> S[i];
    }
    for(int i = 0; i < N; i++) { 
        cin >> T[i];
    }

    for(int i = 0; i < N; i++) {
        if(strcmp(S[i], T[i]) != 0) {
            cout << i + 1 << endl;
            break;
        }
    }

    return 0;
}