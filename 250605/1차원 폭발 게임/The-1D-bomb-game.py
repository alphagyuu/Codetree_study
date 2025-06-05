N,M=map(int,input().split())
bombs=[int(input()) for _ in range(N)]

def explosion(s,combo):
    global bombs
    bombs=bombs[:s]+bombs[s+combo:]


def boom(M):
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
                to_explode.append((s,combo))
            combo=1
            s=i
            curn=newn
    if combo>=M:
        to_explode.append((s,combo))
    if len(to_explode)==0:
        return True
    for s,combo in to_explode:
        explosion(s,combo)
    return False

done=False

while not done:
    done=boom(M)

print(len(bombs))
for b in bombs:
    print(b)