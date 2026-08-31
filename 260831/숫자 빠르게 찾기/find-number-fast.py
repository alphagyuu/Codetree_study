import bisect

N,M=map(int,input().split())
arr=list(map(int,input().split()))

def find(target):
    l, r = 0,N-1
    while l <= r:
        mid =(l+r)//2
        if arr[mid] == target:
            return mid+1
        elif arr[mid] > target:
            r = mid - 1
        else:
            l = mid + 1
    return -1


for _ in range(M):
    x = int(input())
    print(find(x))