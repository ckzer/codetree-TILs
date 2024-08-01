#include <iostream>
#include <string>
using namespace std;

int main() {
    int n, cnt=0;
    double avg=0;
    string arr[20];
    char a;
    
    cin>>n;
    for(int i=0;i<n;i++)    cin>>arr[i];
    cin>>a;

    for(int i=0;i<n;i++) {
        if(arr[i][0]==a) {
            cnt+=1;
            avg+=arr[i].length();
        }
    }
    // printf("%d %.2f", cnt, avg/cnt);
    cout << cnt << " ";
    cout << fixed;
    cout.precision(2);
    cout << avg/cnt;

    return 0;
}