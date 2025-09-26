import heapq

N,M,K=map(int,input().split())

ns=list(map(int,input().split()))

ms=list(map(int,input().split()))

heapq.heapify(ns)
heapq.heapify(ms)

ncnt=1
mcnt=1
tot=1
seln=[heapq.heappop(ns)]
selm=[heapq.heappop(ms)]

while tot<K:
    if not ns or (ms and (ms[0]+seln[0])<(ns[0]+selm[0])):
        selm.append(heapq.heappop(ms))
        mcnt+=1
    else:
        seln.append(heapq.heappop(ns))
        ncnt+=1
    tot=mcnt*ncnt

pq=[]

for i in range(ncnt):
    for j in range(mcnt):
        heapq.heappush(pq,seln[i]+selm[j])

for _ in range(K-1):
    heapq.heappop(pq)

print(pq[0])