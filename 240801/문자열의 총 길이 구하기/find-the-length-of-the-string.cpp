#include <iostream>
#include <string>
using namespace std;

int main() {
    int cnt=0;
    string a[10];
    for(int i=0;i<10;i++) {
        cin>>a[i];
    }
    for(int i=0;i<10;i++) {
        cnt+=a[i].length();
    }
    cout<<cnt;
    return 0;
}