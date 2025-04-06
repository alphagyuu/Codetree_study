N=int(input())
comb=tuple(map(int,input().split()))
keys=[]
for i in range(1,N+1):
    for j in range(1,N+1):
        keys=keys+[(c,i,j) for c in range((max(1,comb[0]-2)),min(N,comb[0]+2)+1)]
        keys=keys+[(i,c,j) for c in range((max(1,comb[1]-2)),min(N,comb[1]+2)+1)] 
        keys=keys+[(i,j,c) for c in range((max(1,comb[2]-2)),min(N,comb[2]+2)+1)]
print(len(set(keys)))


