#include <iostream>
#include <vector>
using namespace std;

int main() {
    int N;
    cin >> N;
    vector<long long> dp(N+1);
    dp[0] = 1;
    for (int n = 1; n <= N; n++) {
        for (int i = 0; i < n; i++) {
            dp[n] += dp[i] * dp[n - 1 - i];
        }
    }
    cout << dp[N] << endl;
    return 0;
}