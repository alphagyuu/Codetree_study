#include <iostream>
using namespace std;

int main() {
    int a[3][3]={0};
    int i,j;
    for(i=0;i<3;i++) {
        for(j=0;j<3;j++) {
            cin >> a[i][j];
        }
    }
    for(i=0;i<3;i++) {
        for(j=0;j<3;j++) {
            cout << a[i][j]*3 << " ";
        }
        cout << "\n";
    }
    return 0;
}