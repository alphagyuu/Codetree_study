rects=[list(map(int,input().split())) for _ in range(3)]
x_min=min([x1 for x1,_,_,_ in rects])
x_max=max([x2 for _,_,x2,_, in rects])
y_min=min([y1 for _,y1,_,_ in rects])
y_max=max([y2 for _,_,_,y2 in rects])

x_OFFSET=-x_min
y_OFFSET=-y_min
axis=[
    [0]*(x_max-x_min+1)
    for _ in range(y_max-y_min+1)
]

for x1,y1,x2,y2 in rects[0:2]:
    for x in range(x1,x2):
        for y in range(y1,y2):
            axis[y+y_OFFSET][x+x_OFFSET]=1
for x in range(rects[2][0],rects[2][2]):
    for y in range(rects[2][1],rects[2][3]):
        axis[y+y_OFFSET][x+x_OFFSET]=0
tot=0
for xs in axis:
    tot+=xs.count(1)
print(tot)