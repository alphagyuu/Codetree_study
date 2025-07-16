#include <iostream>
#include <vector>
#include <string>
using namespace std;

//void push_back(vector<int> &v, )

int main() {
    int N;
    cin >> N;
    vector<int> v;
    int i, val;
    string command;
    for(i=0;i<N;i++) {
        cin >> command;
        if(command=="push_back") {
            cin >> val;
            v.push_back(val);
        }
        else if(command=="pop_back") {
            v.pop_back();            
        }
        else if(command=="size") {
            cout << v.size() << "\n";
        }
        else {
            cin >> val;
            cout << v[val-1] << "\n";
        }
    }
    return 0;
}