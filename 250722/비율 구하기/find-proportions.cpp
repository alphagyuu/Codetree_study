#include <iostream>
#include <map>
using namespace std;

int main() {
    int n, i;
    double tot=0;
    cin >> n;
    string input_s;
    map<string,int> m;
    for(i=0;i<n;i++) {
        cin >> input_s;
        m[input_s]++;
        tot++;
    }
    for(map<string,int>::iterator it=m.begin();it!=m.end();it++) {
        cout << it->first << " ";
        cout << fixed;
        cout.precision(4);
        cout << it->second*100/tot << "\n";
    }
    return 0;
}