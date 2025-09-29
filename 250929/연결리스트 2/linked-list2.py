class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

def pop(x):
    if x.prev is not None:
        x.prev.next = x.next
    if x.next is not None:
        x.next.prev = x.prev
    x.prev = None
    x.next = None

def insert_prev(u,x):
    x.prev=u.prev
    x.next=u
    if x.prev is not None:
        x.prev.next=x
    if x.next is not None:
        x.next.prev=x

def insert_next(u,x):
    x.prev=u
    x.next=u.next
    if x.prev is not None:
        x.prev.next=x
    if x.next is not None:
        x.next.prev=x

N = int(input())

i2N = dict()

for i in range(N):
    cur=Node(i+1)
    i2N[i+1] = cur

Q = int(input())

for _ in range(Q):
    cmd=list(map(int,input().split()))
    c=cmd[0]
    if c==1:
        i=cmd[1]
        pop(i2N[i])
    elif c==2:
        i=cmd[1]
        j=cmd[2]
        insert_prev(i2N[i],i2N[j])
    elif c==3:
        i=cmd[1]
        j=cmd[2]
        insert_next(i2N[i],i2N[j])
    else:
        i=cmd[1]
        print(0 if i2N[i].prev==None else i2N[i].prev.data, end = " ")
        print(0 if i2N[i].next==None else i2N[i].next.data)

for i in range(1,N+1):
    print(0 if i2N[i].next==None else i2N[i].next.data, end = " ")