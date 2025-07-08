#include <iostream>
using namespace std;

int main() {
    char arr[10];
    int i;
    for(i=0;i<10;i++) {
        cin >> arr[i];
    }
    for(i=9;i>=0;i--) {
        cout << arr[i];
    }
}