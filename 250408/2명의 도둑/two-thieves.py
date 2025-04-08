"""
7,1보다
8

2칸씩 순회 -> C안넘치는 제곱의 합을 시작 좌표와 매핑 {(0,0):5 ...} 이런식으로.
"""


N,M,C=map(int,input().split())
grid=[
    list(map(int,input().split()))
    for _ in range(N)
]
#print(grid)
ms={}
for r in range(N):
    for c in range(N-1):
        weight=0
        value=0
        part=sorted([grid[r][c],grid[r][c+1]],reverse=True)
        for i in range(2):
            if weight+part[i]>C:
                continue
            else:
                weight+=part[i]
                value+=part[i]**2
        #print(grid)
        #print(part)
        #print(weight)
        #print(value)
        ms[(r,c)]=value
mlist=list(ms.items())
mlist.sort(key=lambda item: item[1],reverse=True)
#print(mlist[0:3])
if mlist[0][0][0]==mlist[1][0][0] and abs(mlist[0][0][1]-mlist[1][0][1])==1:
    print(mlist[0][1]+mlist[2][1])
else:
    print(mlist[0][1]+mlist[1][1])
#print(ms)

