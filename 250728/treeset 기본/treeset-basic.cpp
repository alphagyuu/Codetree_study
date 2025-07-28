#include <iostream>
#include <set>

using namespace std;

int main() {
    set <int> s;
    int n, x, i;
    string cmd;
    cin >> n;
    for(i=0;i<n;i++) {
        cin >> cmd;
        if(cmd=="add") {
            cin >> x;
            s.insert(x);
        }
        else if(cmd=="remove") {
            cin >> x;
            s.erase(x);
        }
        else if(cmd=="find") {
            cin >> x;
            if(s.find(x)!=s.end()) {
                cout << "true" << "\n";
            }
            else {
                cout << "false" << "\n";
            }
        }
        else if(cmd=="lower_bound") {
            cin >> x;
            if(s.lower_bound(x)!=s.end()) {
                cout << *s.lower_bound(x) << "\n";
            }
            else {
                cout << "None" << "\n";
            }
        }
        else if(cmd=="upper_bound") {
            cin >> x;
            if(s.upper_bound(x)!=s.end()) {
                cout << *s.upper_bound(x) << "\n";
            }
            else {
                cout << "None" << "\n";
            }
        }
        else if(cmd=="largest") {
            if(s.empty()) {
                cout << "None" << "\n";
            }
            else {
                cout << *s.rbegin() << "\n";
            }
        }
        else {
            if(s.empty()) {
                cout << "None" << "\n";
            }
            else {
                cout << *s.begin() << "\n";
            }
        }
    }
    return 0;
}