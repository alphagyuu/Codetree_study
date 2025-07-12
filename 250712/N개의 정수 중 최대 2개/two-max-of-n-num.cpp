#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int N,i;
    cin >> N;
    int a[N]={};
    for(i=0;i<N;i++) {
        cin >> a[i];
    }
    sort(a,a+N);
    cout << a[N-1] << " " << a[N-2];
    return 0;
}