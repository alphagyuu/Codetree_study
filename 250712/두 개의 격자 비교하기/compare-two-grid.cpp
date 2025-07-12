#include <iostream>
using namespace std;

int main() {
    int n, m, r, c;
    cin >> n >> m;
    int arr0[n][m] = {0};
    int arr1[n][m] = {0};
    for(r=0;r<n;r++) {
        for(c=0;c<m;c++) {
            cin >> arr0[r][c];
        }
    }
    for(r=0;r<n;r++) {
        for(c=0;c<m;c++) {
            cin >> arr1[r][c];
        }
    }
    for(r=0;r<n;r++) {
        for(c=0;c<m;c++) {
            if(arr0[r][c]==arr1[r][c]) {
                cout << "0 ";
            }
            else {
                cout << "1 ";
            }
        }
        cout << "\n";
    }
}