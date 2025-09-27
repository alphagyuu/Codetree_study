#include <iostream>
#include <set>
#include <utility>
#include <unordered_map>
using namespace std;

int main() {
    int N, T;
    cin >> N >> T;
    set<pair<int,int>> s;
    unordered_map<int,pair<int,int>> i2ss;
    unordered_map<int,int> i2e;
    for(int i=0;i<N;i++) {
        int start,speed;
        cin >> start >> speed;
        int end = start + speed*T;
        s.insert(make_pair(speed,start));
        i2ss[i]=make_pair(speed,start);
        i2e[i]=end;
    }
    for(int i=0;i<N;i++) {
        int speed,start,end;
        pair<int,int> ss = i2ss[i];
        speed = ss.first, start = ss.second;
        end = i2e[i];
        for(int j=i+1;j<N;j++) {
            if(i2e.find(j)!=i2e.end() & i2e[j]<=end) {
                i2e.erase(i);
                break;
            }
        }
    }
    cout << i2e.size();
    return 0;
}