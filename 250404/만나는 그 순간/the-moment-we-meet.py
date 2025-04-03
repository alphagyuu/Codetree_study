ln,lm=map(int,input().split())
amove=[
    list(map(str,input().split()))
    for _ in range(ln)
]
amove=[[D,int(x)] for D,x in amove]
bmove=[
    list(map(str,input().split()))
    for _ in range(lm)
]
bmove=[[D,int(x)] for D,x in bmove]

def move(amove,bmove):
    apos=0
    bpos=0
    for t in range(1,sum([x for D,x in amove])+1):
        if amove[0][0]=="R":
            apos+=1
        else:
            apos-=1
        amove[0][1]-=1
        if amove[0][1]==0:
            amove=amove[1:]
        if bmove[0][0]=="R":
            bpos+=1
        else:
            bpos-=1
        bmove[0][1]-=1
        if bmove[0][1]==0:
            bmove=bmove[1:]
        if apos==bpos:
            return t
    return -1
print(move(amove,bmove))

        