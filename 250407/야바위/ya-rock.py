N=int(input())
turns=[
    list(map(int,input().split()))
    for _ in range(N)
]
max_cnt=0
for i in range(3):
    cups=[0,0,0,0]
    cups[i+1]=1
    cnt=0
    for a,b,c in turns:
        cups[a],cups[b]=cups[b],cups[a]
        if cups[c]==1:
            cnt+=1
    if max_cnt<cnt:
        max_cnt=cnt
print(max_cnt)

