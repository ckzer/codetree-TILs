#include <iostream>
#include <string>
using namespace std;

int main() {
    string arr[5] = {"apple", "banana", "grape", "blueberry", "orange"};
    char tmp;
    int cnt=0;
    cin >> tmp;
    for(int i=0;i<5;i++) {
        if(arr[i][2] == tmp || arr[i][3] == tmp) {
            cnt++;
            cout << arr[i] << "\n";
        }
    }
    cout << cnt;
    return 0;
}