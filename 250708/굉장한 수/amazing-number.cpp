#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;
    if((n%3==0 and n%2!=0) || (n%5==0 and n%2==0)) {
        cout <<"true";
    }
    else {
        cout <<"false";
    }
}