#include <iostream>
#include <map>
using namespace std;

int main() {
    int n, i, k, v;
    string input_s;
    cin >> n;
    map<int,int> m;
    for(i=0;i<n;i++) {
        cin >> input_s;
        if(input_s=="add") {
            cin >> k >> v;
            m[k]=v;
        }
        else if(input_s=="remove") {
            cin >> k;
            m.erase(k);
        }
        else if(input_s=="find") {
            cin >> k;
            if(m.find(k)==m.end()) {
                cout << "None";
            }
            else {
                cout << m[k];
            }
            cout << "\n";
        }
        else {
            if(m.empty()) {
                cout << "None";
            }
            else {
                for(map<int,int>::iterator it = m.begin();it!=m.end();it++) {
                    cout << it->second << " ";
                }
                cout << "\n";
            }
        }
    }
    return 0;
}