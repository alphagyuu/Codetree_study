#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_map>
using namespace std;

int main() {
    int N, Q, i;
    cin >> N >> Q;
    vector<int> nums(N);
    unordered_map<int,int> m;
    for(i=0;i<N;i++) {
        cin >> nums[i];
    }
    sort(nums.begin(),nums.end());
    for(i=0;i<N;i++) {
        m[nums[i]] = i;
    }
    for(i=0;i<Q;i++) {
        int a, b;
        cin >> a >> b;
        cout << m[b]-m[a]+1 << "\n";
    }
    return 0;
}