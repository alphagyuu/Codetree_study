#include <iostream>
#include <unordered_set>
using namespace std;

int main() {
    int an, bn, i, x;
    cin >> an >> bn;
    unordered_set<int> a,b,c;
    for(i=0;i<an;i++) {
        cin >> x;
        a.insert(x);
    }
    for(i=0;i<bn;i++) {
        cin >> x;
        b.insert(x);
    }
    for(unordered_set<int>::iterator it = a.begin();it!=a.end();it++) {
        if(b.find(*it)==b.end()) {
            c.insert(*it);
        }
    }
    for(unordered_set<int>::iterator it = b.begin();it!=b.end();it++) {
        if(a.find(*it)==a.end()) {
            c.insert(*it);
        }
    }
    cout << c.size();
    return 0;
}