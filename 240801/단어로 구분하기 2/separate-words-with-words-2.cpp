#include <iostream>
#include <string>
using namespace std;

int main() {
    string arr[10];
    for(int i=0;i<10;i++) {
        cin>>arr[i];
        if(i%2==0)  cout<<arr[i]<<"\n";
    }
    return 0;
}