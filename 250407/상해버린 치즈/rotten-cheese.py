N,M,D,S=map(int,input().split())
dininglist=[
    list(map(int,input().split()))
    for _ in range(D)
] #p m t

sicklist=[
    list(map(int,input().split()))
    for _ in range(S)
] #p t

sickp=[x[0] for x in sicklist]
#print(sickp)

eatbeforesick=[
    [0]*len(sickp)
    for _ in range(M+1)
]

for p,m,t in dininglist:
    if p in sickp:
        if t<sicklist[sickp.index(p)][1]:
            eatbeforesick[m][sickp.index(p)]=1

#print(eatbeforesick)
might_be_rotten=[]
for i in range(M+1):
    if sum(eatbeforesick[i])==len(sickp):
        might_be_rotten.append(i)

#print(might_be_rotten)
might_be_sick=[0]*(N+1)
for p,m,t in dininglist: 
    if m in might_be_rotten:
        might_be_sick[p]=1
print(sum(might_be_sick))