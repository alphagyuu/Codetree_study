#include <iostream>
using namespace std;

int main() {
    int chu=13;
    double g=0.165000;
    cout << chu;
    cout << fixed;
    cout.precision(6);
    cout << " * " << g << " = " << chu*g;
}