#include <iostream>
using namespace std;

int main() {
    int N1,N2;
    cin >> N1 >> N2;
    int a1[N1] = {}, a2[N2] = {};
    int i;
    for(i=0;i<N1;i++) {
        cin >> a1[i];
    }
    for(i=0;i<N2;i++) {
        cin >> a2[i];
    }
    int combo=0;
    int si=0;
    for(i=0;i<N1;i++) {
        if(combo==0) {
            if (a1[i]==a2[0]) {
                combo++;
            }
        }
        else {
            if(a1[i]==a2[combo]) {
                combo++;
            }
            else {
                combo=0;
            }
        }
        if(combo>=N2) {
            cout << "Yes";
            return 0;
        }
    }
    cout << "No";
    return 0;
}