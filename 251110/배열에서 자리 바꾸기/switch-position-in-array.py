class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

def insert_next(u,x):
    x.prev = u
    x.next = u.next
    if x.prev is not None:
        x.prev.next = x
    if x.next is not None:
        x.next.prev = x

def pop_range_insert_next(s,e,i):
    if s.prev is not None:
        s.prev.next = e.next
    if e.next is not None:
        e.next.prev = s.prev
    
    s.prev = i
    e.next = i.next
    if s.prev is not None:
        s.prev.next = s
    if e.next is not None:
        e.next.prev = e

N = int(input())
Q = int(input())

i2N = dict()

for i in range(N+2):
    cur=Node(i)
    i2N[i] = cur

for i in range(1,N+2):
    insert_next(i2N[i-1],i2N[i])

for _ in range(Q):
    a,b,c,d = map(int,input().split())
    temp = i2N[a].prev

    pop_range_insert_next(i2N[a],i2N[b],i2N[d])
    pop_range_insert_next(i2N[c],i2N[d],temp)


cur = i2N[0]

while cur.next.data<N+1:
    cur = cur.next
    print(cur.data, end = " ")
