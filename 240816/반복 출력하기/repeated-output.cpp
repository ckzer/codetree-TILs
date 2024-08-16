#include <iostream>
using namespace std;

void PrintString(int n) {
    for(int i=0;i<n;i++) {
        cout << "12345^&*()_" << "\n";
    }
}

int main() {
    int n;
    cin >> n;
    PrintString(n);
    return 0;
}