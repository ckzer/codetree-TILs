#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int Div(int n) {
    int sum=0;
    for(int i=1;i<=n;i++) {
        sum+=i;
    }
    sum/=10;
    return sum;
}

int main() {
    int n;
    cin >> n;
    cout << Div(n);
    return 0;
}