#include <iostream>
#include <string>
using namespace std;

int main() {
    string arr;
    int n, len;
    cin >> arr >> n;
    len = arr.length()-1;
    for(int i=len; i>len-n; i--) cout<<arr[i];
    return 0;
}