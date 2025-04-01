ln,lm=map(int,input().split())
nlist=list(map(int,input().split()))
mlists=[
    list(map(int,input().split()))
    for _ in range(lm)
]
for i in range(lm):
    print(sum(nlist[(mlists[i][0]-1):(mlists[i][1])]))