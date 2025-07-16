#include <iostream>
#include <vector>
using namespace std;

// 3x3 부분합 계산 함수
int count3x3(int R, int C, const vector<vector<int>>& grid) {
    int tot = 0;
    for (int r = R; r < R + 3; ++r) {
        for (int c = C; c < C + 3; ++c) {
            tot += grid[r][c];
        }
    }
    return tot;
}

int main() {
    int n;
    cin >> n;

    vector<vector<int>> grid(n, vector<int>(n));  // n x n 2차원 벡터

    // 입력 받기
    for (int r = 0; r < n; ++r) {
        for (int c = 0; c < n; ++c) {
            cin >> grid[r][c];
        }
    }

    int top = 0;
    for (int r = 0; r <= n - 3; ++r) {
        for (int c = 0; c <= n - 3; ++c) {
            int temp = count3x3(r, c, grid);
            top = max(top, temp);
        }
    }

    cout << top << endl;
    return 0;
}