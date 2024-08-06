#include <iostream>
#include <string>
using namespace std;

int main() {
    string s, first="No", second="No";
    cin >> s;
    if(s.find("ee") != string::npos)   first="Yes";
    if(s.find("ab") != string::npos)   second="Yes";
    cout << first << " " << second;

    return 0;
}