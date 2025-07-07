#include <iostream>
using namespace std;

int main() {
    int a,b;
    cin >> a >> b;
    cout << fixed;
    cout.precision(1); //precision은 실수 자료형에만 적용된다!!
    cout << a+b << " " << double(a+b)/2;
}