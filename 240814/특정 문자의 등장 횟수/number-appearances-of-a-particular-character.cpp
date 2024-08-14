#include <iostream>
#include<string>
using namespace std;

int main() {
    string cnt;
    int first, second;
    cin>>cnt;
    if(cnt.find("ee")) first++;
    else if(cnt.find("eb")) second++;
    cout<<first<<" "<<second;
    return 0;
}