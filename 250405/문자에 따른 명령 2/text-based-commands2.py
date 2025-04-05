moves=list(input())
#print(moves)
dx=[0,1,0,-1]
dy=[1,0,-1,0]

head=0
pos=[0,0]
for m in moves:
    if m=="R":
        head=(head+1)%4
    elif m=="L":
        head=(head-1)%4
    else:
        pos[0]+=dx[head]
        pos[1]+=dy[head]
print(*pos)