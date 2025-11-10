class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

def connect(s,e): # *****connect 함수는 순서 매우중요 (앞, 뒤) 순서 안지키면 error)
    if s is not None:
        s.next = e
    if e is not None:
        e.prev = s

def swap(a,b,c,d):
    ap = a.prev
    bn = b.next
    cp = c.prev
    dn = d.next
    
    if bn == c:
        cp = d
        bn = a

    if dn == a:
        ap = b
        dn = c

    connect(cp,a)
    connect(b,dn)
    connect(ap,c)
    connect(d,bn)

N = int(input())
Q = int(input())

node = dict()

for i in range(N+1):
    node[i] = Node(i)

for i in range(N):
    connect(node[i],node[i+1])

for _ in range(Q):
    qs = list(map(int,input().split()))
    a,b,c,d = tuple(node[q] for q in qs)
    swap(a,b,c,d)

cur = node[0]
while cur.next!=None:
    cur = cur.next
    print(cur.data, end = " ")

#Spaghetti
'''
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

def debug():
    cur = i2N[0]
    while cur.next.data<N+1:
        cur = cur.next
        print(cur.data, end = " ")
    print("")


for _ in range(Q):
    a,b,c,d = map(int,input().split())
    temp = i2N[a].prev
    if temp.data == d:
        temp = i2N[c].prev
        pop_range_insert_next(i2N[c],i2N[d],i2N[b])
        #debug()
        pop_range_insert_next(i2N[a],i2N[b],temp)
        #debug()    

    else: 
        pop_range_insert_next(i2N[a],i2N[b],i2N[d])
        #debug()
        pop_range_insert_next(i2N[c],i2N[d],temp)
        #debug()    

debug()
'''