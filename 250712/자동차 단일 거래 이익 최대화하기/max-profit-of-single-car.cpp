#include <iostream>
using namespace std;

int main() {
    int N,i;
    cin >> N;
    int arr[N];
    for(i=0;i<N;i++) {
        cin >> arr[i];
    }
    int ggul=arr[0], max_p=0;
    for(i=1;i<N;i++) {
        if(arr[i]<ggul) {
            ggul=arr[i];
        }
        else {
            max_p = (arr[i]-ggul) > max_p ? (arr[i]-ggul) : max_p;
        }
    }
    cout << max_p;
    return 0;
}