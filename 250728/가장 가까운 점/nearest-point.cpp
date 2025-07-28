#include <iostream>
#include <queue>
#include <tuple>
using namespace std;

int main() {
    int n, m, i, x, y;
    cin >> n >> m;
    priority_queue<tuple<int,int,int>> pq;
    for(i=0;i<n;i++) {
        cin >> x >> y;
        pq.push(make_tuple(-(x+y),-x,-y));
    }
    for(i=0;i<m;i++) {
        tuple<int,int,int> topdot = pq.top();
        pq.pop();
        pq.push(make_tuple(get<0>(topdot)-4, get<1>(topdot)-2, get<2>(topdot)-2));
    }
    tuple<int,int,int> topdot = pq.top();
    cout << -get<1>(topdot) << " " << -get<2>(topdot);
    return 0;
}