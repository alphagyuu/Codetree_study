ln=int(input())
insts=[
    list(map(str,input().split()))
    for _ in range(ln)
]
insts=[[int(x),D] for x,D in insts]
#print(insts)

front=sum([x for x,D in insts if D=="L"])
back=sum([x for x,D in insts if D=="R"])
#print(front,back)
axis=["e"]*(front+back+1)

pos=front-1
for x,D in insts:
    if D=="R":
        for i in range(pos,pos+x):
            axis[i]="b"
        pos=pos+x-1
    else:
        for i in range(pos,pos-x,-1):
            axis[i]="w"
        pos=pos-x+1
print(axis.count("w"),axis.count("b"))