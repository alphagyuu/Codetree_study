N,K,P,T=map(int,input().split())
#K: 전염력
#P: 발원지
#T: 총 시간

infected=[0]*N
infected[P-1]=1
remains=[K]*N

shakes=[
    list(map(int,input().split()))
    for _ in range(T)
]
shakes.sort(key=lambda x:x[0])
#print(shakes)

for t,x,y in shakes:
    x-=1
    y-=1
    iy=infected[y]
    ix=infected[x]
    if infected[x]==1:
        if remains[x]>0:
            iy=1
            remains[x]-=1
    if infected[y]==1:
        if remains[y]>0:
            ix=1
            remains[y]-=1
    infected[x]=ix
    infected[y]=iy
    #print(t,x,y)
    #print(remains)
print("".join([str(x) for x in infected]))
    