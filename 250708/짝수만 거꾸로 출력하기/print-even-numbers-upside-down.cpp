#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;
    int a[n] = {0};
    int i;
    for(i=0;i<n;i++) {
        cin >> a[i];
    }
    for(i=n-1;i>=0;i--) {
        if(a[i]%2==0) {
            cout << a[i] << " ";
        }
    }
    return 0;
}