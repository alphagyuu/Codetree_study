N=int(input())
houses=list(map(int,input().split()))
ds=[]
for i in range(len(houses)):
    d_sum=0
    for j in range(len(houses)):
        d_sum+=abs(j-i)*houses[j]
    ds.append(d_sum)
print(min(ds))