#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int n;

vector<int> step;

int Makenn(int i, int x) {
    if(i==0) {
        return x-1;
    }
    else if(i==1) {
        return x+1;
    }
    else if(i==2 && x%2==0) {
        return x/2;
    }
    else if(i==3 && x%3==0) {
        return x/3;
    }
    else {
        return -1;
    }
}

int Search() {
    queue<int> q;
    q.push(n);
    step[n]=0;
    while(!q.empty()) {
        int cur_n=q.front();
        q.pop();
        int cur_step=step[cur_n], i;
        for(i=0;i<4;i++) {
            int nn=Makenn(i,cur_n);
            if(nn==-1) {
                continue;
            }
            if(nn<n*2 && step[nn]==-1) {
                step[nn]=cur_step+1;
                q.push(nn);
                if(nn==1) {
                    return cur_step+1;
                }
            }
        }
    }
    return -1;
}

int main() {
    cin >> n;
    step.resize(n*2,-1);
    cout << Search();
}