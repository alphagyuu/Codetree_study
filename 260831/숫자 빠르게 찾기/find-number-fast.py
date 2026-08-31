import bisect

N,M=map(int,input().split())
arr=list(map(int,input().split()))

for _ in range(M):
    x = int(input())
    i = bisect.bisect_left(arr,x)
    if i < N and arr[i] == x:
        print(i+1)
    else:
        print(-1)