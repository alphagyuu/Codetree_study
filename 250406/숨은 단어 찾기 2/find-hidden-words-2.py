ln,lm=map(int,input().split())
box= [
    list(input())
    for _ in range(ln)
]

def in_box(x,y):
    if x>=0 and y>=0 and x<lm and x<ln:
        return True
    else:
        return False


dxs=[1,1,1,0,0,-1,-1,-1]
dys=[1,0,-1,1,-1,1,0,-1]
lee=["L","E","E"]
count=0
for i in range(ln):
    for j in range(lm):
        turn=0
        x=i
        y=i
        for dx,dy in zip(dxs,dys):
            if box[y][x]==lee[turn]:
                turn+=1
            else:
                turn=0
            if turn==2:
                count+=1
                turn=0
            if in_box(x+dx,y+dy):
                x+=dx
                y+=dy
            else:
                break
print(count)