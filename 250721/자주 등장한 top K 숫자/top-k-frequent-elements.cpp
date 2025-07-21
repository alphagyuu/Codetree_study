#include <iostream>
#include <unordered_map>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int N, K, i, x;
    cin >> N >> K;
    unordered_map<int,int> times;
    for(i=0;i<N;i++) {
        cin >> x;
        if(times.count(x)==0) {
            times[x]=1;
        }
        else {
            times[x]+=1;
        }
    }
    vector<pair<int,int>> v;
    for(unordered_map<int,int>::iterator it = times.begin(); it != times.end(); it++) {
        v.push_back(make_pair(it->first, it->second));
    }
    sort(v.begin(),v.end(), [](pair<int,int> a, pair<int,int> b) {
        if (a.second == b.second) return a.first > b.first;
        return a.second > b.second;
    });
    for (i = 0; i < K; i++) {
        cout << v[i].first << " ";
    }
    return 0;
}