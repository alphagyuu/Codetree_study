#include <iostream>
#include <unordered_map>

using namespace std;

void func(string s, unordered_map<char,int> m) {
    int i;
    for(i=0;i<s.length();i++) {
        if(m[s[i]]==1) {
            cout << s[i];
            return;
        }
    }
    cout << "None";
    return;
}

int main() {
    string s;
    cin >> s;
    unordered_map<char,int> m;
    int i;
    for(i=0;i<s.length();i++) {
        m[s[i]]++;
    }
    func(s,m);
    return 0;
}