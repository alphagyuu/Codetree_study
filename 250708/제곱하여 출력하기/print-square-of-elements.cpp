#include <iostream>
using namespace std;

int main() {
    int n,i;
    cin >> n;
    int a[n] = {0};
    for(i=0;i<n;i++) {
        cin >> a[i];
    }
    for(i=0;i<n;i++) {
        cout << a[i]*a[i] << " ";
    }
}