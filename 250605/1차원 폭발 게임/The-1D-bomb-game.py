N,M=map(int,input().split())
bombs=[int(input()) for _ in range(N)]


def boom(M):
    global bombs
    if len(bombs)==0:
        return True
    curn=bombs[0]
    combo=1
    s=0
    to_explode=[]
    for i in range(1,len(bombs)):
        newn=bombs[i]
        if newn==curn:
            combo+=1
        else:
            if combo>=M:
                for x in range(combo):
                    to_explode.append(x+s)
            combo=1
            s=i
            curn=newn
    if combo>=M:
        for x in range(combo):
            to_explode.append(x+s)
    if len(to_explode)==0:
        return True
    for i in to_explode:
        bombs[i]=0
    temp=[]
    for i in range(len(bombs)):
        if bombs[i]>0:
            temp.append(bombs[i])
    bombs=temp
    return False

done=False

while not done:
    done=boom(M)

print(len(bombs))
for b in bombs:
    print(b)