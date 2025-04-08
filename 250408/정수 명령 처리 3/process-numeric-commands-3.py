from collections import deque

dq=deque()

def process(instruction):
    inst=instruction[0]
    if len(instruction)>1:
        val=instruction[1]
    if inst=="push_front":
        dq.appendleft(val)
    elif inst=="push_back":
        dq.append(val)
    elif inst=="pop_front":
        print(dq.popleft())
    elif inst=="pop_back":
        print(dq.pop())
    elif inst=="size":
        print(len(dq))
    elif inst=="empty":
        print(0 if dq else 1)
    elif inst=="front":
        print(dq[0])
    elif inst=="back":
        print(dq[-1])
    return 0


N=int(input())
insts=[list(map(str,input().split())) for _ in range(N)]
for inst in insts:
    process(inst)