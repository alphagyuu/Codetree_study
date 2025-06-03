N,T=map(int,input().split())

belt=[]
for _ in range(2):
    belt+=list(map(int,input().split()))


for _ in range(T):
    last=belt[-1]
    for i in range(4,-1,-1):
        belt[i+1]=belt[i]
    belt[0]=last


for i in range(3):
    print(belt[i],end=" ")
print("")
for i in range(3,6):
    print(belt[i],end=" ")