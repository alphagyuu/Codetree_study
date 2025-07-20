#include <iostream>
#include <unordered_map>

using namespace std;

int main() {
    unordered_map<int,int> m;
    int n, i, k, v;
    cin >> n;
    string cmd;
    for(i=0;i<n;i++) {
        cin >> cmd;
        if(cmd=="add") {
            cin >> k >> v;
            m[k]=v;
        }
        else if(cmd=="remove") {
            cin >> k;
            m.erase(k);
        }
        else {
            cin >> k;
            if(m.find(k)==m.end()) {
                cout << "None";
            }
            else {
                cout << m[k];
            }
            cout << "\n";
        }
    }
    return 0;
}