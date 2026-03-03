#include <iostream>
using namespace std;

int main() {
    int x, sum = 0;
    for(int i = 0; i<10; i++) {
        cin >> x;
        sum += x;
    }
    cout << sum;
    return 0;
}