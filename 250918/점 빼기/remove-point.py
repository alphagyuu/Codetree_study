from sortedcontainers import SortedSet

N,M=map(int,input().split())

s=SortedSet()

for _ in range(N):
    x,y=map(int,input().split())
    s.add((x,y))

for _ in range(M):
    k=int(input())
    idx=s.bisect_left((k,0))
    if idx==len(s):
        print("-1 -1")
    else:
        print(f"{s[idx][0]} {s[idx][1]}")
        s.remove(s[idx])