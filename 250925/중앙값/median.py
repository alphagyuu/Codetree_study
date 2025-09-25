import heapq

T = int(input())

for _ in range(T):
    M=int(input())
    ns=list(map(int,input().split()))
    #mid=ns[0]
    low=[]
    high=[]
    heapq.heappush(low,-0)
    heapq.heappush(high,100001)
    for i in range(M):
        if i%2==0:
            mid=ns[i]
            if low[0]<-mid:
                heapq.heappush(low,-mid)
                mid=-heapq.heappop(low)
            if high[0]<mid:
                heapq.heappush(high,mid)
                mid=heapq.heappop(high)
            print(mid, end=" ")
        else:
            heapq.heappush(low,-min(mid,ns[i]))
            heapq.heappush(high,max(mid,ns[i]))
    print('')

'''
m / 3 / M

m / 1,3 / M

1/ 3 /5
'''