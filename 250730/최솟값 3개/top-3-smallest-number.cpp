#include <iostream>
#include <queue>
using namespace std;

priority_queue<int> pq;
int main() {
    int n, x, i, a, b, c;
    cin >> n;
    for(i=0;i<n;i++) {
        cin >> x;
        pq.push(-x);
        if(i<2) {
            cout << -1 << "\n";
            continue;
        }
        a = -pq.top();
        pq.pop();
        b = -pq.top();
        pq.pop();
        c = -pq.top();
        cout << (long long)a*b*c << "\n";
        pq.push(-a);
        pq.push(-b);
    }
    return 0;
}