#include <iostream>
using namespace std;

int main() {
    int a,b;
    cin >> a >> b;
    double ans;
    ans= (double) (a+b)/(a-b);
    cout << fixed;
    cout.precision(2);
    cout << ans;
    return 0;
}