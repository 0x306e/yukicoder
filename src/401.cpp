using namespace std;
#include "bits/stdc++.h"

int main(){
    int N;
    int array[31][31];
    cin >> N;
    int num = 0;
    int cnt = 0;
    for(int i = 0; i < N; i++){
        array[i][0] = i+1;
        num++;
    }
    while(num<N*N){
        for(int i = 0; i < N - cnt * 2 - 1; i++){
            array[N-cnt-1][cnt+i] = num;
            num++;
        }
        for(int i = 0; i < N - cnt * 2 - 1; i++){
            array[N-cnt-1-i][N-cnt-1] = num;
            num++;
        }
        for(int i = 0; i < N - cnt * 2 - 2; i++){
            array[cnt][N-i-cnt-1] = num;
            num++;
        }
        for(int i = 0; i < N - cnt * 2 - 2; i++){
            array[cnt+i][cnt+1] = num;
            num++;
        }
        cnt++;
    }
    if (N % 2 == 1){
        array[(N-1)/2][(N-1)/2] = N * N;
    } else {
        array[(N-1)/2][(N-1)/2 + 1] = N * N;
    }

    for(int i = 0; i < N; i++){
        for(int j = 0; j < N; j++){
            cout << setfill('0') << setw(3) << right << array[j][i] << ' ';
        }
        cout << endl;
    }
    return 0;
}