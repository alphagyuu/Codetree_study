#include <iostream>
using namespace std;

int main() {
    string a,b;
    cin >> a >> b;
    int la,lb;
    la=a.length();
    lb=b.length();
    if(la>lb) {
        cout << a << " " << la;
    }
    else if (lb>la) {
        cout << b << " " << lb;
    }
    else {
        cout << "same";
    }
    return 0;
}