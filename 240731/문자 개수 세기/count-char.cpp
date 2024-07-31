#include <iostream>
#include <string>
#include <bits/stdc++.h>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    string a;
    char b;
    int cnt=0;
    getline(cin, a);
    cin>>b;
    for(int i=0;i<a.length();i++) {
        if(a[i]==b) cnt++;
    }
    cout<<cnt;
    return 0;
}