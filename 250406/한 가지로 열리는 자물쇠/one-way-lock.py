N=int(input())
comb=tuple(map(int,input().split()))
keys=0
for i in range(1,N+1):
    for j in range(1,N+1):
        for k in range(1,N+1):
            if i in range((max(1,comb[0]-2)),min(N,comb[0]+2)+1) or j in range((max(1,comb[1]-2)),min(N,comb[1]+2)+1) or k in range((max(1,comb[2]-2)),min(N,comb[2]+2)+1):
                keys+=1

print(keys)


