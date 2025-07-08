#include <iostream>
using namespace std;

int main() {
    int n,i,tot;
    cin >> n;
    tot=0;
    for(i=1;tot<=n;i++) {
        tot+=i;
    }
    cout << i-1;
}