def is_possible(k):
    global ns, M
    cnt = 0
    for n in ns:
        cnt += n//k
    return cnt>=M

N, M = map(int,input().split())
ns = [int(input()) for _ in range(N)]

left = 0
right = sum(ns)
max_k = -1

while left <= right:
    mid = (left + right) // 2
    if is_possible(mid):
        max_k = max(mid, max_k)
        left = mid + 1
    else:
        right = mid - 1
        

print(max_k)

