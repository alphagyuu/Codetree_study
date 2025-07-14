#include <iostream>
#include <string>
#include <algorithm>
#include <functional>
using namespace std;

int main() {
    int n,i;
    cin >> n;
    string a[n];
    for(i=0;i<n;i++) {
        cin >> a[i];
    }
    sort(a,a+n);
    for(i=0;i<n;i++) {
        cout << a[i] << "\n";
    }
    return 0;
}