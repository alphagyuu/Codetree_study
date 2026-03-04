#include <iostream>
using namespace std;

int main() {
    int x, tot;
    for(int i = 0; i<4; i++) {
        tot = 0;
        for(int j = 0; j<4; j++) {
            cin >> x;
            tot += x;
        }
        cout << tot << "\n";
    }
    return 0;
}