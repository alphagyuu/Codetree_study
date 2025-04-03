ln=int(input())
rects=[tuple(map(int,input().split())) for _ in range(ln)]
xs=[x1 for x1,_,_,_ in rects]+[x2 for _,_,x2,_ in rects]
ys=[y1 for _,y1,_,_ in rects]+[y2 for _,_,_,y2 in rects]
XOFFSET=-(min(xs))
YOFFSET=-(min(ys))
axis=[
    [0]*(max(xs)-min(xs)+1)
    for _ in range(max(ys)-min(ys)+1)
]
for x1,y1,x2,y2 in rects:
    for x in range(x1,x2):
        for y in range(y1,y2):
            axis[y+YOFFSET][x+XOFFSET]=1
tot=0
for x in axis:
    tot+=x.count(1)
print(tot)