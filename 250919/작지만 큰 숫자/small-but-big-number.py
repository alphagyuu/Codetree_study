from sortedcontainers import SortedSet

N, M = map(int,input().split())

ns=list(map(int,input().split()))

ms=tuple(map(int,input().split()))

s=SortedSet(ns)

for m in ms:
    idx=s.bisect_right(m)
    if idx == 0:
        print(-1)
    else:
        print(s[idx-1])
    s.remove(s[idx-1])