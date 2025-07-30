#include <iostream>
#include <queue>
#include <algorithm>
#include <tuple>
using namespace std;


int main() {
    int n;
    int i, a, t;
    cin >> n;
    priority_queue<tuple<int,int,int>> people;
    for(i=1;i<n+1;i++) {
        cin >> a >> t;
        people.push(make_tuple(-a,-i,t));
    }
    priority_queue<tuple<int,int,int>> wait;
    int max_taken=0, cur_time=0;
    while(!people.empty() || !wait.empty()) {
        // 1. 현재 시간까지 도착한 사람들 대기열에 넣기
        while (!people.empty() && -get<0>(people.top()) <= cur_time) {
            auto p = people.top();
            people.pop();
            wait.push(make_tuple(get<1>(p), get<0>(p), get<2>(p)));  // 번호순 우선
        }

        if (!wait.empty()) {
            // 2. 대기열 가장 앞사람 입장
            auto w = wait.top(); wait.pop();
            int wait_time = cur_time + get<1>(w);
            max_taken = max(max_taken, wait_time);
            cur_time += get<2>(w);  // 머무는 시간
        } else if (!people.empty()) {
            // 3. 아직 아무도 안 왔으면 가장 빨리 도착하는 사람까지 시간 점프
            auto p = people.top();
            people.pop();
            cur_time = -get<0>(p);
            wait.push(make_tuple(get<1>(p), get<0>(p), get<2>(p)));  // push 후 다음 loop에서 처리
        }
    }
    cout << max_taken;
    return 0;
}