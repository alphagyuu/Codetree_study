#include <iostream>
#include <queue>
using namespace std;

int main() {
    int n, i, a;
    priority_queue<int> pq;
    string cmd;
    cin >> n;
    for(i=0;i<n;i++) {
        cin >> cmd;
        if(cmd=="push") {
            cin >> a;
            pq.push(a);
        }
        else if(cmd=="pop") {
            cout << pq.top() << "\n";
            pq.pop();
        }
        else if(cmd=="size") {
            cout << pq.size() << "\n";
        }
        else if(cmd=="empty") {
            if(pq.empty()) {
                cout << 1 << "\n";
            }
            else {
                cout << 0 << "\n";
            }
        }
        else {
            cout << pq.top() << "\n";
        }
    }
    return 0;
}