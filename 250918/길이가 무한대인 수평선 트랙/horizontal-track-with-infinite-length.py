# 그룹 개수만 알면 되니까 만나면 소멸시키기.

#start가 큰데 end가 작거나 같으면 -> 소멸 

from sortedcontainers import SortedSet

N,T=map(int,input().split())

ss=SortedSet()
ssidx=dict()
i2e=dict()


for i in range(N):
    start,speed=map(int,input().split())
    ss.add((speed,start))
    ssidx[i]=(speed,start)
    end=start+speed*T
    i2e[i]=end


for i in range(N):
    speed,start=ssidx[i]
    end=i2e[i]
    for j in range(i+1,N):
        if j in i2e and i2e[j]<=end:
            ss.remove((speed,start))
            i2e.pop(i)
            break

print(len(ss))
