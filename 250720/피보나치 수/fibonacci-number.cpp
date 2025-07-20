#include <iostream>
#include <vector>

using namespace std;

int n;
vector<int> dp = {0,1,1};

int main() {
    cin >> n;
    dp.resize(n+1);
    int i;
    for(i=2;i<=n;i++) {
        dp[i]=dp[i-1]+dp[i-2];
    }
    cout << dp[n];
    return 0;
}