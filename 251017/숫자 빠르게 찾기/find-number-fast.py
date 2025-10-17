N,M=map(int,input().split())
Ns=list(map(int,input().split()))
for _ in range(M):
    m = int(input())
    left, right = 0,N-1
    while left<=right:
        mid = (left+right)//2
        if Ns[mid] == m:
            break
        elif Ns[mid] < m:
            left = mid + 1
        else:
            right = mid - 1
    print(mid+1 if Ns[mid] == m else -1)