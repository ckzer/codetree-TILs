#include <iostream>
#include <string>
using namespace std;

int main() {
    string init, arr;
    
    cin >> init;
    for(int i=1;i<init.length();i+=2) {
        arr+=init[i];
    }
    for(int i=arr.length()-1; i>=0; i--)    cout << arr[i];
    
    return 0;
}