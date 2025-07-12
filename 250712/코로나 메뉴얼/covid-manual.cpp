#include <iostream>
using namespace std;

int main() {
    int i;
    char js;
    int temp, cnt;
    cnt=0;
    for(i=0;i<3;i++) {
        cin >> js >> temp;
        if(js=='Y' && temp>=37) {
            cnt+=1;
        }
    }
    if(cnt>=2) {
        cout << "E";
    }
    else {
        cout << "N";
    }
    return (0);
}