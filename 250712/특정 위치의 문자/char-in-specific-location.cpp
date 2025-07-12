#include <iostream>
#include <string>
using namespace std;

int main() {
    string lebros = "LEBROS";
    char s;
    cin >> s;
    int loc=-1,i;
    for(i=0;i<(sizeof(lebros)/sizeof(lebros[0]));i++) {
        if(lebros[i]==s) {
            loc=i;
            break;
        }
    }
    if(loc<0) {
        cout << "None";
    }
    else {
        cout << loc;
    }
    return 0;
}