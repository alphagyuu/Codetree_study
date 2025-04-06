N=int(input())
OFFSET=1000000
arr=[0]*(OFFSET*2+1)
lines=[
    tuple(map(int,input().split()))
    for _ in range(N)
]
for x1,x2 in lines:
    for x in range(x1,x2):
        arr[x+OFFSET]+=1
cnt=0
for x1,x2 in lines:
    #print(arr[x1+OFFSET:x2+OFFSET])
    check=arr[x1+OFFSET+1:x2+OFFSET-1]
    if x2-x1==1 and arr[x1+OFFSET]>1:
        continue
    elif max(check)>arr[x1+OFFSET] or max(check)>arr[x2+OFFSET-1]:
        continue
    else:
        cnt+=1
print(cnt)