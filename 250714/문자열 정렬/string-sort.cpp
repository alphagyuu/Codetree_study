#include <iostream>
#include <string>
#include <algorithm>
#include <functional>

using namespace std;

int main() {
    string a;
    cin >> a;
    sort(a.begin(),a.end());
    //sort(a.begin(),a.end(),greater<char>());
    cout << a;
}