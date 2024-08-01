#include <iostream>
#include <string>
using namespace std;

int main() {
    int n, cnt=0, len=0;
    string str;
    cin >> n;
    for(int i=0;i<n;i++) {
        cin >> str;
        len += str.length();
        if (str[0]=='a') cnt++;
    }
    cout << len << " " << cnt;
    return 0;
}