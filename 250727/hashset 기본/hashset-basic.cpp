#include <iostream>
#include <unordered_set>
using namespace std;

unordered_set<int> s;

int main() {
    int N;
    cin >> N;
    string c;
    int x, i;
    for(i=0;i<N;i++) {
        cin >> c >> x;
        if(c=="add") {
            s.insert(x);
        }
        else if(c=="remove") {
            s.erase(x);
        }
        else {
            if(s.find(x) != s.end()) {
                cout << "true" << "\n";
            }
            else {
                cout<< "false" << "\n";
            }
        }
    }
    return 0;
}