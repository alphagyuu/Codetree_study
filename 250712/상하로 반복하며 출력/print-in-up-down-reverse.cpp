#include <iostream>
using namespace std;

int main() {
    int N,r,c,i,j;
    cin >> N;
    int arr[N][N]={0};
    c=0;
    for(c=0;c<N;c++) {
        int x=0;
        if(c%2==0) {
            for(r=0;r<N;r++) {
                x++;
                arr[r][c]=x;
            }
        }
        else {
            for(r=N-1;r>=0;r--) {
                x++;
                arr[r][c]=x;
            }
        }
    }
    for(r=0;r<N;r++) {
        for(c=0;c<N;c++) {
            cout<<arr[r][c];
        }
        cout << "\n";
    }
    return 0;
}