#include <iostream>
#include <queue>
using namespace std;

int main() {
    int t, m, i, test_cases, x;
    cin >> t;
    for(test_cases=0;test_cases<t; test_cases++) {
        cin >> m;
        priority_queue<int> maxHeap;
        priority_queue<int> minHeap;
        for(i=0;i<m;i++) {
            cin >> x;
            if (maxHeap.empty() || x <= maxHeap.top()) maxHeap.push(x);
            else minHeap.push(-x);
            if (maxHeap.size() > minHeap.size() + 1) {
                minHeap.push(-maxHeap.top());
                maxHeap.pop();
            }
            else if (minHeap.size() > maxHeap.size()) {
                maxHeap.push(-minHeap.top());
                minHeap.pop();
            }
            if(i%2==0) {
                cout << maxHeap.top() << " ";
            }
        }
        cout << "\n";
    } 
    return 0;
}