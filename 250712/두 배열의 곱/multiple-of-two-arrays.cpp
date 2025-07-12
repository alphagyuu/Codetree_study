#include <iostream>
using namespace std;

int main() {
    int arr[3][3] = {0};
    int arr2[3][3] = {0};
    int r,c;
    for(r=0;r<3;r++) {
        for(c=0;c<3;c++) {
            cin >> arr[r][c];
        }
    }
    for(r=0;r<3;r++) {
        for(c=0;c<3;c++) {
            cin >> arr2[r][c];
        }
    }
    for(r=0;r<3;r++) {
        for(c=0;c<3;c++) {
            cout << arr[r][c] * arr2[r][c] << " ";
        }
        cout << "\n";
    }
}