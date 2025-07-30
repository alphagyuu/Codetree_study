#include <iostream>
#include <queue>
using namespace std;

int main() {
    int n, i, x;
    cin >> n;
    int nums[100000];
    priority_queue<int> pq;
    long long tot=0;
    double max_avg = 0;
    for(i=0;i<n;i++) {
        cin >> nums[i];
    }
    pq.push(-nums[n-1]);
    tot+=nums[n-1];
    for(i=n-2;i>=0;i--) {
        pq.push(-nums[i]);
        tot+=nums[i];
        double avg = (double)(tot+pq.top())/(n-1-i);
        if(max_avg < avg) {
            max_avg = avg;
        }
    }
    cout << fixed;
    cout.precision(2);
    cout << max_avg;
    return 0;
}