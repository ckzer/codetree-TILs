#include <iostream>
#include <string>
using namespace std;

int main() {
    string arr[10]={};
    int n;
    cin >> n;
    for(int i=0;i<n;i++) {
        cin >> arr[i];
    }
    for(int i=0;i<n;i++) {
        cout << arr[i];
    }
    return 0;
}