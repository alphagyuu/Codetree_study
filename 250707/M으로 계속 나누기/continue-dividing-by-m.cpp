#include <iostream>
using namespace std;

int main() {
    int n,m;
    cin >> n >> m;
    while(n>0) {
        cout << n << "\n";
        n = n/m;
    }
    return 0;
}