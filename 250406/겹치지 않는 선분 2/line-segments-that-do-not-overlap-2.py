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
    check=arr[x1+OFFSET:x2+OFFSET]
    is_valid=True
    for i in range(x2-x1):
        for j in range(i+1,x2-x1):
            if check[i]==check[j] and check[i]!=0:
                is_valid=False
    if is_valid:
        cnt+=1
print(cnt)


