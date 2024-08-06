#include <iostream>
#include <string>
using namespace std;

int main() {
    int n;
    string hap, cnt;
    cin>>n;
    for(int i=0;i<n;i++) {
        cin>>cnt;
        hap+=cnt;
    }
    for(int i=0;i<hap.length();i++) {
        if (i>0 && i%5==0) {
            cout<<"\n";
        }
        cout << hap[i];
    }
    return 0;
}