#include <iostream>
using namespace std;

int main() {
    int N;
    cin >> N;
    int a[N], i;
    for(i=0;i<N;i++) {
        cin >> a[i];
        if(a[i]%2==0) {
            a[i]/=2;
        }
        cout << a[i] << " ";
    }

    return 0;
}