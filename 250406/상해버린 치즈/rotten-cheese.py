N,M,D,S=map(int,input().split())
dininglist=[
    list(map(int,input().split()))
    for _ in range(D)
] #p m t

sicklist=[
    list(map(int,input().split()))
    for _ in range(S)
] #p t

m_isrotten=[0]*(M+1)
n_might_be_siick=[0]*(N+1)

for p,m,t in dininglist:
    sickp=[x[0] for x in sicklist]
    if p in sickp:
        if t < sicklist[sickp.index(p)][1]:
            m_isrotten[m]=1
#print(m_isrotten)
for p,m,t in dininglist:
    if m_isrotten[m]==1:
        n_might_be_siick[p]=1
        
print(n_might_be_siick.count(1))
    
