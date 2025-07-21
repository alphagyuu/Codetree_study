#include <iostream>
#include <map>
#include <string>
#include <unordered_map>

using namespace std;

int main() {
    int N, i, j;
    string s;
    cin >> N;
    map<char,int> freq;
    unordered_map<string,int> groups;
    for(i=0;i<N;i++) {
        cin >> s;
        freq.clear();
        string k = "";
        for(j=0;j<s.size();j++) {
            freq[s[j]]++;
        }
        for(map<char,int>::iterator it = freq.begin(); it!=freq.end();it++) {
            k+=it->first;
            k+=to_string(it->second);
        }
        groups[k]++;
    }
    int top=0;
    for(unordered_map<string,int>::iterator it = groups.begin();it!=groups.end();it++) {
        top=max(top,it->second);
    }
    cout << top;
    
    return 0;
}