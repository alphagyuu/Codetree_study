ln=int(input())
axis=[
    list(map(int,input().split()))
    for _ in range(ln)
]

dx=[0,0,1,-1]
dy=[1,-1,0,0]

count=0
for y in range(ln):
    for x in range(ln):
        kan=0
        for i in range(ln):
            if y+dy[i]>=0 and y+dy[i]<ln and x+dx[i]>=0 and x+dx[i]<ln:
                kan+=axis[y+dy[i]][x+dx[i]]
        if kan>=3:
            count+=1
print(count)