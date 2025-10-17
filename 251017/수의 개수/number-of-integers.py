N,M = map(int,input().split())
Ns = list(map(int,input().split()))

def bisect_left(m):
    left, right = 0, N-1
    min_idx = N
    while left <= right:
        mid = (left+right)//2
        if Ns[mid] >= m:
            right = mid - 1
            min_idx = min(mid, min_idx)
        else:
            left = mid + 1
    return min_idx

def bisect_right(m):
    left, right = 0, N-1
    min_idx = N
    while left <= right:
        mid = (left+right)//2
        if Ns[mid] > m:
            right = mid - 1
            min_idx = min(mid,min_idx)
        else:
            left = mid + 1
    return min_idx


for _ in range(M):
    m = int(input())
    l = bisect_left(m)
    r = bisect_right(m)
    print(r-l)