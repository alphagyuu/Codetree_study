#include <iostream>
#include <queue>
using namespace std;

int main() {
    int n,m,i,x;
    priority_queue<int> pq;
    cin >> n >> m;
    for(i=0;i<n;i++) {
        cin >> x;
        pq.push(x);
    }
    for(i=0;i<m;i++) {
        x=pq.top();
        pq.pop();
        x-=1;
        pq.push(x);
    }
    cout << pq.top();
    return 0;
}