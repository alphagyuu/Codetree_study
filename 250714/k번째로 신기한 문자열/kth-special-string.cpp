#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

bool val(string s, string t) {
    int i;
    for(i=0;i<t.length();i++) {
        if(t[i]!=s[i]) {
            return false;
        }    
    }
    return true;
}

int main() {
    int n,k;
    string t;
    cin >> n >> k >> t;
    string strs[n];
    int i;
    for(i=0;i<n;i++) {
        cin >> strs[i];
    }
    sort(strs,strs+n);
    int x=1;
    for(i=0;i<n;i++) {
        if(val(strs[i],t)==false) {
            continue;
        }
        if(x==k) {
            cout << strs[i];
        }
        x++;
    }
    return 0;
}