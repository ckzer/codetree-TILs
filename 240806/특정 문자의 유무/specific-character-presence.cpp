#include <iostream>
#include <string>
using namespace std;

int main() {
    string s, first="No", second="No";
    cin >> s;
    for(int i=0;i<s.length()-1;i++) {
        if(s.find("ee") != string::npos) {
            first="Yes";
        }
        else if(s.find("ab") != string::npos)   second="Yes";
    }
    cout << first << " " << second;

    return 0;
}