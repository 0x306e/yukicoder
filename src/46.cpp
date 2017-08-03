//
// Created by 3sodn on 2017/08/01.
//
#include <iostream>
#include <cmath>
using namespace std;

int main(void) {
    double a, b;
    cin >> a >>  b;
    double tmp = b / a;
    int res = std::ceil(tmp);
    cout << res << endl;

    return 0;
}