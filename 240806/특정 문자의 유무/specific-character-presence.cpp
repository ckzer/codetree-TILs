#include <iostream>
#include <string>
using namespace std;

int main() {
    string s, first="No", second="No";
    cin >> s;
    for(int i=0;i<s.length()-1;i++) {
        if(s.find("ee")) {
            first="Yes";
        }
        else if(s.find("ab"))   second="No";
    }
    cout << first << " " << second;

    return 0;
}