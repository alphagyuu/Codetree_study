#include <iostream>
using namespace std;

int main() {
    int a, n, i;
    cin >> a >> n;
    for(i=0;i<n;i++) {
        a+=n;
        cout << a << "\n";
    }
}