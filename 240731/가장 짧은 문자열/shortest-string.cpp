#include <iostream>
#include <string>
#include <bits/stdc++.h>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    string a, b, c;
    cin >> a >> b >> c;
    int arr[3];
    arr[0] = a.length();
    arr[1] = b.length();
    arr[2] = c.length();
    sort(arr, arr+3);
    cout << arr[2]-arr[0];    
    return 0;
}