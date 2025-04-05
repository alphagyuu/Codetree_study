ln=int(input())
cps=[
    list(map(int,input().split()))
    for _ in range(ln)
]
d=[]
dif=[]
for i in range(ln-1):
    d.append(abs(cps[i+1][1]-cps[i][1])+abs(cps[i+1][0]-cps[i][0]))
    if i<ln-2:
        jeongjik=abs(cps[i+1][1]-cps[i][1])+abs(cps[i+1][0]-cps[i][0])+abs(cps[i+2][1]-cps[i+1][1])+abs(cps[i+2][0]-cps[i+1][0])
        yabi=abs(cps[i+2][1]-cps[i][1])+abs(cps[i+2][0]-cps[i][0])
        dif.append(jeongjik-yabi)

#print(d)
#print(dif)
print(sum(d)-max(dif))