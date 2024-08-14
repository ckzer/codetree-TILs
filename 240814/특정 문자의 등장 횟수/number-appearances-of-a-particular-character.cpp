#include <iostream>
#include<string>
using namespace std;

int main() {
    string cnt;
    int first=0, second=0;
    cin>>cnt;
    for(int i=0;i<cnt.length()-1;i++) {
        if(cnt[i]=='e' && cnt[i+1]=='b') first++;
        else if(cnt[i]=='e' && cnt[i+1]=='e') second++;
    }
    cout<<first<<" "<<second;
    return 0;
}