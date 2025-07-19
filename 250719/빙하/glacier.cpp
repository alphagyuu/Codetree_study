#include <iostream>
#include <vector>
#include <deque>
using namespace std;

int n,m;

vector<vector<int>> grid;
vector<vector<bool>> visited;

vector<pair<int,int>> turn_rcs;

deque<pair<int,int>> active;

bool InGrid(int r, int c) {
    return 0<=r && r<n && 0<=c && c<m;
}

int dr[4]={1,-1,0,0}, dc[4]={0,0,1,-1};

int visit_cnt=0;

void Start(int r=0, int c=0) {
    turn_rcs.clear();
    deque<pair<int,int>> dq;
    dq.push_front(make_pair(r,c));
    visited[r][c]=true;
    turn_rcs.push_back(make_pair(r,c));
    while(!dq.empty()) {
        pair<int,int> curr_pos = dq.front();
        dq.pop_front();
        int r = curr_pos.first, c = curr_pos.second, i;
        for(i=0;i<4;i++) {
            int nr=r+dr[i], nc=c+dc[i];
            if(InGrid(nr,nc) && grid[nr][nc]==0 && (!visited[nr][nc])) {
                dq.push_front(make_pair(nr,nc));
                visited[nr][nc] = true;
                turn_rcs.push_back(make_pair(nr,nc));
            }
        }
    }
}

bool Done() {
    int i,j;
    for(i=0;i<n;i++) {
        for(j=0;j<m;j++) {
            if(grid[i][j]==1) {
                return false;
            }
        }
    }
    return true;
}

int main() {
    cin >> n >> m;
    grid.resize(n,vector<int>(m));
    visited.resize(n,vector<bool>(m,false));
    int i,j;
    for(i=0;i<n;i++) {
        for(j=0;j<m;j++) {
            cin >> grid[i][j];
        }
    }
    

    int turn=0,snr=0,snc=0, cnt;
    while(!Done()) {
        Start(snr,snc);
        cnt=0;
        for(i=0;i<turn_rcs.size();i++) {
            pair<int,int> curr_pos = turn_rcs[i];
            int r = curr_pos.first, c=curr_pos.second;
            for(j=0;j<4;j++) {
                int nr=r+dr[j], nc=c+dc[j];
                if(InGrid(nr,nc) && grid[nr][nc]==1 && (!visited[nr][nc])) {
                    grid[nr][nc]=0;
                    snr=nr,snc=nc;
                    cnt+=1;
                }
            }
        }
    turn+=1;
    }
    cout << turn << " " << cnt;
}

