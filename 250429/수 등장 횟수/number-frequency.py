N,M=map(int,input().split())
nums=list(map(int,input().split()))
ms=list(map(int,input().split()))
counts=dict()
for n in nums:
    if n in counts:
        counts[n]+=1
    else:
        counts[n]=1

for m in ms:
    print(counts.get(m,0),end=" ")