#include <iostream>
#include <string>
using namespace std;

int main() {
    string cnt;
    cin >> cnt;
    cnt[1]='a';
    cnt[cnt.length()-2]='a';
    cout << cnt;
    return 0;
}