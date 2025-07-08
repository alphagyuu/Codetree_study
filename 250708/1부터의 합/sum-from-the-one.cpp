#include <iostream>
using namespace std;

int main() {
    int n,i,tot;
    cin >> n;
    tot=0;
    i=1;
    while(true) {
        tot+=i;
        if(tot>=n) {
            break;
        }
        i++;
    }
    cout << i;
}