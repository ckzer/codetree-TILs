#include <iostream>
#include <bits/stdc++.h>
using namespace std;

#define MAX_N 100
int n;
string a[MAX_N];

int main() {
    cin >> n;
    for (int i=0;i<n;i++) {
        cin >> a[i];
    }
    sort(a, a+n);
    for(int i=0;i<n;i++) {
        cout << a[i]<<"\n";
    }
    return 0;
}