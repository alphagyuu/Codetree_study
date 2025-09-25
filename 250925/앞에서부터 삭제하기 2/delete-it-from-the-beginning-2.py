import heapq

N=int(input())

ns=list(map(int,input().split()))

#print(ns[-2:])
pq=[]

tot=ns[-1]
heapq.heappush(pq,ns[-1])

max_avg=0

for i in range(2,N+1):
    heapq.heappush(pq,ns[-i])
    tot+=ns[-i]
    max_avg=max(max_avg,((tot-pq[0])/(i-1)))

print(f"{max_avg:.2f}")