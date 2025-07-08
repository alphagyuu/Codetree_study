#include <iostream>
using namespace std;

int main() {
    int count = 0;
    int i,n;
    cin >> n;
    for (i=1;i<=n;i++) {
        if(i%2==0 || i%3==0 || i%5==0) {
            continue;
        }
        else {
            count+=1;
        }
    }
    cout << count;
    return 0;
}