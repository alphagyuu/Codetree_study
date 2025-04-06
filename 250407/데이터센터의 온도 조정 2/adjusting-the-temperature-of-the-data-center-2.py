N,C,G,H=map(int,input().split())
equips=[
    list(map(int,input().split()))
    for _ in range(N)
]

max_works=0
for t in range(0,1001):
    works=0
    for t0,t1 in equips:
        if t<t0:
            works+=C
        elif t>t1:
            works+=H
        else:
            works+=G
    if works>max_works:
        max_works=works
print(max_works)