#include <iostream>
#include <string>
using namespace std;

int main() {
    string arr, arr_print="";
    char cnt_char;
    int cnt=0;
    cin >> arr;
    cnt_char=arr[0];
    for(int i=0;i<arr.length();i++) {
        if(cnt_char==arr[i]) {
            cnt++;
            if(i==arr.length()-1) {
                arr_print+=cnt_char;
                arr_print+=to_string(cnt);
            }
        }
        else {
            arr_print+=cnt_char;
            arr_print+=to_string(cnt);
            cnt_char=arr[i];
            cnt=1;
            if(i==arr.length()-1) {
                arr_print+=cnt_char;
                arr_print+=to_string(cnt);
            }
        }
    }
    cout << arr_print.length() << "\n" << arr_print;
    return 0;
}