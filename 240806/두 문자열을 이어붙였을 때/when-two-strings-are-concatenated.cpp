#include <iostream>
#include <string>
using namespace std;

int main() {
    string a, b;
    cin >> a >> b;
    if(a+b!=b+a)    cout << "false";
    else    cout<< "true";
    return 0;
}