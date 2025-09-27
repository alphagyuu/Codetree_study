import heapq

N=int(input())

ait=[]

for i in range(N):
    a,t=map(int,input().split())
    heapq.heappush(ait,(a,i,t))

cur_t=ait[0][0]

iat_waiting=[]

max_wait_time = 0

while True:
    while ait and ait[0][0]<=cur_t:
        a,i,t = heapq.heappop(ait)
        heapq.heappush(iat_waiting,(i,a,t))
    if iat_waiting:
        ci,ca,ct=heapq.heappop(iat_waiting)
        max_wait_time = max(max_wait_time,cur_t-ca)
        cur_t += ct;
    elif not ait:
        break
    else:
        cur_t = ait[0][0]

print(max_wait_time)
    