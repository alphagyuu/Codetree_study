#include <iostream>
using namespace std;

int main() {
    int a[10] = {0};
    cin >> a[0] >> a[1];
    int i;
    cout << a[0] << " " << a[1] << " ";
    for(i=2;i<10;i++) {
        a[i] = (a[i-1]+a[i-2])%10;
        cout << a[i] << " ";
    }
}