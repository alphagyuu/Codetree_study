rects=[
    list(map(int,input().split()))
    for _ in range(2)
]

x1=min(rects[0][0],rects[1][0])
x2=max(rects[0][2],rects[1][2])
y1=min(rects[0][1],rects[1][1])
y2=max(rects[0][3],rects[1][3])

print((max(x2-x1,y2-y1))**2)