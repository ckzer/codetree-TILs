#include <iostream>
#include <string>
using namespace std;

int main() {
    string a, b;
    int check=-1;

    cin >> a >> b;
    if(a.find(b)!=string::npos) check=a.find(b);
    cout<<check;
    
    return 0;
}