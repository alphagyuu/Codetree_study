N,M = map(int,input().split())
Ns = list(map(int,input().split()))
for _ in range(M):
    m = int(input())
    print(Ns.count(m))