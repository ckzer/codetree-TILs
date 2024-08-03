#include <iostream>
#include <string>
using namespace std;

int main() {
    string init;
    
    cin >> init;
    for(int i=init.length()-1; i>=0; i-=2)  cout << init[i];
    return 0;
}