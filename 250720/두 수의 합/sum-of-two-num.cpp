#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

#define MAX_N 100000

// 변수 선언
int n, k;
vector<int> v;
unordered_map<int, int> count;

int main() {
    // 입력:
    cin >> n >> k;
    v.resize(n);
    for(int i = 0; i < n; i++)
        cin >> v[i];

    int ans = 0;

    // 배열을 앞에서부터 순회하며 쌍을 만들어줍니다.
    for(int i = 0; i < n; i++) {
        int diff = k - v[i];
        // 가능한 모든 쌍의 수를 세어줍니다.
        ans += count[diff];

        // 현재 숫자의 개수를 하나 증가시켜줍니다.
        count[v[i]]++;
    }

    cout << ans;
    return 0;
}
