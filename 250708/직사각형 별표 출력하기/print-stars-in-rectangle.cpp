#include <iostream>
using namespace std;

int main() {
    int n,m,r,c;
    cin >> n >> m;
    for(r=0;r<n;r++) {
        for(c=0;c<m;c++) {
            cout << "* ";
        }
        cout << "\n";
    }
    return 0;
}