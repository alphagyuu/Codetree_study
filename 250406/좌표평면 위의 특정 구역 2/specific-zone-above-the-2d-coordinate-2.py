N=int(input())
dots=[
    tuple(map(int,input().split()))
    for _ in range(N)
]
for i in range(len(dots)):
    x1=min([x for x,y in dots[0:i]+dots[i+1:]])
    x2=max([x for x,y in dots[0:i]+dots[i+1:]])
    y1=min([y for x,y in dots[0:i]+dots[i+1:]])
    y2=max([y for x,y in dots[0:i]+dots[i+1:]])
    arr=(x2-x1)*(y2-y1)
    if i==0:
        min_arr=arr
    else:
        if min_arr>arr:
            min_arr=arr
print(min_arr)