#include <iostream>
using namespace std;

int main() {
    int i,j,N;
    cin >> N;
    j=0;
    for(i=0;i<N;i++) {
        if(j==0) {
            for(j=1;j<=N;j++) {
                cout << j;
            }
        }
        else {
            for(j=N;j>0;j--) {
                cout << j;
            }
        }
        cout << "\n";
    }
    return 0;
}