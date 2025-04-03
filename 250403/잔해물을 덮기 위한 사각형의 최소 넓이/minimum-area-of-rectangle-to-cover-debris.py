rects=[tuple(map(int,input().split())) for _ in range(2)]
x_min=min(x1 for x1,_,_,_ in rects)
x_max=max(x2 for _,_,x2,_ in rects)
y_min=min(y1 for _,y1,_,_ in rects)
y_max=max(y2 for _,_,_,y2 in rects)
xOFFSET=-x_min
yOFFSET=-y_min
axis=[
    [0]*(x_max-x_min+1)
    for _ in range(y_max-y_min+1)
]
for i in range(1,-1,-1):
    x1,y1,x2,y2=tuple(rects[abs(i-1)])
    for x in range(x1,x2):
        for y in range(y1,y2):
            axis[y+yOFFSET][x+xOFFSET]=i
        
x1,x2,y1,y2=len(axis[0])-1,0,len(axis)-1,0
for y in range(len(axis)):
    for x in range(len(axis[0])):
        if axis[y][x]==1:
            if x<x1:
                x1=x
            if x>x2:
                x2=x
            if y<y1:
                y1=y
            if y>y2:
                y2=y
print((x2-x1+1)*(y2-y1+1))