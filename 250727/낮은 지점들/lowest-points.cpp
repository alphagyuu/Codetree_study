#include <iostream>
#include <unordered_map>

using namespace std;

unordered_map<int,int> dots;

int main(){
    int N;
    cin >> N;
    int x,y,i;
    for(i=0;i<N;i++) {
        cin >> x >> y;
        if(dots.find(x) == dots.end()) {
            dots[x]=y;
        }
        else {
            dots[x]=min(dots[x],y);
        }
    }
    long long tot=0;
    for(unordered_map<int,int>::iterator it = dots.begin(); it!=dots.end(); it++) {
        tot+=it->second;
    }
    cout << tot;
    return 0;
}