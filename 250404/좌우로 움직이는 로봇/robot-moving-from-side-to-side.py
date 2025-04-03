ln,lm=map(int,input().split())
amove=[
    input().split()
    for _ in range(ln)
]
bmove=[
    input().split()
    for _ in range(lm)
]
amove=[[int(t),d] for t,d in amove]
bmove=[[int(t),d] for t,d in bmove]
apos=0
bpos=0
end=False
count=0
while not end:
    if not amove[0][1]=="X":
        if amove[0][1]=="R":
            apos+=1
        else:
            apos-=1
        amove[0][0]-=1


    if not bmove[0][1]=="X":
        if bmove[0][1]=="R":
            bpos+=1
        else:
            bpos-=1
        bmove[0][0]-=1
    

    if amove[0][1]!=bmove[0][1] and apos==bpos:
        count+=1

    #print(amove[0],bmove[0],apos,bpos,count)

    if amove[0][1]=="X" and bmove[0][1]=="X":
        end=True
    else:
        if amove[0][0]==0:
            if len(amove)==1:
                amove[0][1]="X"
            else:
                amove=amove[1:]
        if bmove[0][0]==0:
            if len(bmove)==1:
                bmove[0][1]="X"
            else:
                bmove=bmove[1:]


print(count)