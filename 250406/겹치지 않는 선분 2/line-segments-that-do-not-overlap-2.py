N=int(input())

lines=[
    tuple(map(int,input().split()))
    for _ in range(N)
]
l_val=[0]*N

for i in range(N):
    for j in range(i+1,N):
        ax1,ax2=lines[i]
        bx1,bx2=lines[j]
        if (bx1<ax1 and ax2<bx2) or (ax1<bx1 and ax2<bx2):
            l_val[i]=1
print(l_val.count(0))


