#include <iostream>
using namespace std;

/*
int check(string & given, string & part) {
    int i,j;
    bool find=false;
    for(i=0;i<=(given.length()-part.length());i++) {
        find = true;
        for(j=0;j<part.length();j++) {
            if(given[i+j]!=part[j]) {
                find = false;
                break;
            }
        }
        if(find) {
            return i;
        }
    }
    return -1;
}

int main() {
    string given, part;
    cin >> given >> part;
    cout << check(given,part);
    return 0;
}
*/
int check(string &given,string &part) {
    return given.find(part);
}

int main() {
    string given, part;
    cin >> given >> part;
    cout << check(given,part);
    return 0;
}