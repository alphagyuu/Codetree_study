ln=int(input())
rects=[
    list(map(int,input().split()))+["r" if i%2==0 else "b"]
    for i in range(ln)
]
#print(rects)

x_min=min([x1 for x1,_,_,_,_ in rects])
x_max=max([x2 for _,_,x2,_,_ in rects])
y_min=min([y1 for _,y1,_,_,_ in rects])
y_max=max([y2 for _,_,_,y2,_ in rects])

axis=[
    ["e"]*(x_max-x_min+1)
    for i in range(y_max-y_min+1)
]

for x1,y1,x2,y2,c in rects:
    for x in range(x1,x2):
        for y in range(y1,y2):
            axis[y-y_min][x-x_min]=c

blue_count=0
for xs in axis:
    blue_count+=xs.count("b")
print(blue_count)