N=int(input())
dots=[
    tuple(map(int,input().split()))
    for _ in range(N)
]
for i in range(N):
    for j in range(i+1,N):
        x1,y1=dots[i]
        x2,y2=dots[j]
        dis=(x1-x2)**2+(y1-y2)**2
        if i==0 and j==1:
            min_dis=dis
        elif min_dis>dis:
            min_dis=dis
print(min_dis)