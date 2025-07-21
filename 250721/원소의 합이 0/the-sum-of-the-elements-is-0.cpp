#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

vector<int> a,b,c,d;
unordered_map<int,int> freq;

int main() {
    int N, i, j, x;
    cin >> N;
    for(i=0;i<N;i++) {
        cin >> x;
        a.push_back(x);
    }
    for(i=0;i<N;i++) {
        cin >> x;
        b.push_back(x);
    }
    for(i=0;i<N;i++) {
        cin >> x;
        c.push_back(x);
    }
    for(i=0;i<N;i++) {
        cin >> x;
        d.push_back(x);
    }
    int ans = 0;
    for(int i = 0; i < N; i++)
        for(int j = 0; j < N; j++)
            freq[a[i] + b[j]]++;
    
    for(int i = 0; i < N; i++)
        for(int j = 0; j < N; j++) {
            int diff = - c[i] - d[j];
            if(freq.count(diff) > 0)
                ans += freq[diff];
        }
    cout << ans;
    return 0;
}