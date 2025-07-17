#include <iostream>
#include <vector>
using namespace std;

int count3x3(int R,int C,vector<vector<int>> & grid) {
    int r,c,tot=0;
    for(r=R;r<R+3;r++) {
        for(c=C;c<C+3;c++) {
            if(grid[r][c]==1) {
                tot++;
            }
        }
    }
    return tot;
}

int main() {
    int n;
    cin >> n;
    vector<vector<int>> grid(n,vector<int>(n));
    int temp,top=0,r,c;
    for(r=0;r<n;r++) {
        for(c=0;c<n;c++) {
            cin >> grid[r][c];
        }
    }
    for(r=0;r<n-2;r++) {
        for(c=0;c<n-2;c++) {
            temp=count3x3(r,c,grid);
            top=temp>top?temp:top;
        }
    }
    cout << top;
    return 0;
}