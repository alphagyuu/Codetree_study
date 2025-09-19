import heapq

N=int(input())

hq=[]

for _ in range(N):
    inst=input().split()
    c=inst[0]
    if c=="push":
        heapq.heappush(hq,-int(inst[1]))
    elif c=="pop":
        x=heapq.heappop(hq)
        print(-x)
    elif c=="size":
        print(len(hq))
    elif c=="empty":
        if hq:
            print(0)
        else:
            print(1)
    else:
        print(-hq[0])