ln=int(input())
moves=[
    list(map(str,input().split()))
    for _ in range(ln)
]
def moveto(move):
    directions=["N","S","W","E"]
    dx=[0,0,-1,1]
    dy=[1,-1,0,0]
    i=directions.index(move[0])
    return (dx[i]*int(move[1]),dy[i]*int(move[1]))

x=0
y=0
for move in moves:
    x+=moveto(move)[0]
    y+=moveto(move)[1]
print(x,y)