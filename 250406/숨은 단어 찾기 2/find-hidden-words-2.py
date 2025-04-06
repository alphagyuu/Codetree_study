ln,lm=map(int,input().split())
box= [
    list(input())
    for _ in range(ln)
]

def in_box(x,y):
    if x>=0 and y>=0 and x<lm and y<ln:
        return True
    else:
        return False


dxs=[1,1,1,0,0,-1,-1,-1]
dys=[1,0,-1,1,-1,1,0,-1]
lee=["L","E","E"]
count=0
for i in range(ln):
    for j in range(lm):
        for dx,dy in zip(dxs,dys):
            x=j
            y=i
            turn=0
            for k in range(3):
                if box[y][x]==lee[turn]:
                    turn+=1
                else:
                    turn=0
                if turn==3:
                    count+=1
                    turn=0
                if in_box(x+dx,y+dy):
                    x+=dx
                    y+=dy
                else:
                    break
print(count)