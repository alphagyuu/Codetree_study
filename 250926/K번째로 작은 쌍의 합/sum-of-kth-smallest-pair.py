import heapq

N,M,K=map(int,input().split())

ns=list(map(int,input().split()))

ms=list(map(int,input().split()))

heapq.heapify(ns)
heapq.heapify(ms)

seln=[]
selm=[]

tot=0
ncnt=0
mcnt=0
TOT=min(M*N,100000)
while tot<TOT:
    if not ms or ns[0]>ms[0]:
        seln.append(heapq.heappop(ns))
        ncnt+=1
    else:
        selm.append(heapq.heappop(ms))
        mcnt+=1
    tot=ncnt*mcnt

pq=[]

for i in range(ncnt):
    for j in range(mcnt):
        heapq.heappush(pq,(seln[i]+selm[j]))

for _ in range(K-1):
    heapq.heappop(pq)

print(pq[0])