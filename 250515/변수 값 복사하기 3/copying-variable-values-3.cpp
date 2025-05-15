#include <iostream>
using namespace std;

int main() {
    int a = 1, b = 5, c = 3;
    a = c;
    a = a + c;
    b = b - c;
    cout << a;
    cout << "\n";
    cout << b;
    cout << "\n";
    cout << c;
    return 0;
}