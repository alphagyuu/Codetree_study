#include <iostream>
#include <climits>
using namespace std;

int main() {
    int N,i,m;
    cin >> N;
    int a[N], mi;
    for(i=0;i<N;i++) {
        cin >> a[i];
    }
    while(N>0) {
        m=INT_MIN;
        mi=0;
        for(i=0;i<N;i++) {
            if(m<a[i]) {
                mi=i;
                m=a[i];
            }
        }
        cout << mi+1 << " ";
        N=mi;
    }
    return 0;
}