#include <iostream>
#include <string>
using namespace std;

string is_palindrome(string &a) {
    int i;
    for(i=0;i<((a.length()+1)/2);i++) {
        if(a[i]!=a[a.length()-1-i]) {
            return "No";
        }
    }
    return "Yes";
}

int main() {
    string a;
    cin >> a;
    cout << is_palindrome(a);
    return 0;
}