#include <iostream>
#include <string>
using namespace std;

int main() {
    string arr[10];
    char a;
    int check=0;
    for(int i=0;i<10;i++)   cin>>arr[i];
    cin>>a;
    for(int i=0;i<10;i++) {
        if(arr[i][arr[i].length()-1]==a){
            cout<<arr[i]<<"\n";
            check=1;
        }
    }
    if(check==0)    cout<<"None";

    return 0;
}