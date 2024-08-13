#include <iostream>
#include <string>
using namespace std;

int main() {
    string arr;
    char a;
    int check=-1;
    cin >> arr >> a;
    if(arr.find(a)!=string::npos) {
        check=arr.find(a);
    }
    if(check==-1) cout<<"No";
    else cout<<check;
    
    return 0;
}