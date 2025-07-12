#include <iostream>
using namespace std;

int main() {
    int a,b;
    cin >> a >> b;
    int cnt[b] = {};
    while(a>1) {
        cnt[a%b]++;
        a/=b;
    }
    int ans=0,i;
    for(i=0;i<b;i++) {
        ans+=cnt[i]*cnt[i];
    }
    cout<<ans;
    return 0;
}