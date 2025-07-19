#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int n,m;

vector<vector<int>> grid;
vector<vector<int>> step;

int dr[4] = {1,-1,0,0}, dc[4] = {0,0,1,-1};

bool InGrid(int r, int c) {
    return 0<=r && r<n && 0<=c && c<m;
}

int BFS(int r=0,int c=0) {
    vector<vector<int>> visited(n,vector<int>(m,false));
    queue<pair<int,int>> q;
    q.push(make_pair(r,c));
    visited[r][c]=true;
    step[r][c]=0;
    while(!q.empty()) {
        pair<int,int> curr_dir = q.front();
        q.pop();
        r=curr_dir.first, c=curr_dir.second;
        int curr_step=step[r][c];
        int i;
        for(i=0;i<4;i++) {
            int nr=r+dr[i], nc=c+dc[i];
            if(InGrid(nr,nc) && grid[nr][nc]==1 && (!visited[nr][nc])) {
                q.push(make_pair(nr,nc));
                visited[nr][nc]=true;
                step[nr][nc]=curr_step+1;
                if(nr==n-1 && nc==m-1) {
                    return curr_step+1;
                }
            }
        }
    }
    return -1;
}

int main() {
    cin >> n >> m;
    grid.resize(n,vector<int>(m));
    step.resize(n,vector<int>(m,0));
    int i,j;
    for(i=0;i<n;i++) {
        for(j=0;j<m;j++) {
            cin >> grid[i][j];
        }
    }
    cout << BFS();
    return 0;
}