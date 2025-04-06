N=int(input())
OFFSET=1000000
arr=[0]*(OFFSET*2+1)
lines=[
    tuple(map(int,input().split()))
    for _ in range(N)
]
i=1
for x1,x2 in lines:
    arr[x1+OFFSET]=i
    arr[x2+OFFSET-1]=i
    i+=1
cnt=0
for x1,x2 in lines:
    is_valid=True
    seen=[]
    for i in range(x2-x1):
        val=arr[i+x1+OFFSET]
        if val in seen:
            is_valid=False
        if val!=0:
            seen.append(val)
    if is_valid:
        cnt+=1
print(cnt)


