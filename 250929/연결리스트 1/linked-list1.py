class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None

def insert_next(u,x):
    x.prev=u
    x.next=u.next
    if x.prev is not None:
        x.prev.next=x
    if x.next is not None:
        x.next.prev=x

def insert_prev(u,x):
    x.prev=u.prev
    x.next=u
    if x.prev is not None:
        x.prev.next=x
    if x.next is not None:
        x.next.prev=x

def pop(u):
    if u.prev is not None:
        u.prev.next=u.next
    if u.next is not None:
        u.next.prev=u.prev
    u.prev = u.next = None

s_init=input()
N=int(input())

cur=Node(s_init)

for _ in range(N):
    cmd=input().split()
    cmd[0]=int(cmd[0])
    if cmd==1:
        s=cmd[1]
        insert_prev(cur,Node(s))
    elif cmd==2:
        s=cmd[1]
        insert_next(cur,Node(s))
    elif cmd==3:
        if cur.prev is not None:
            cur=cur.prev
    else:
        if cur.next is not None:
            cur=cur.next
    print("Null" if cur.prev==None else cur.prev.data,end=" ") 
    print("Null" if cur==None else cur.data,end=" ") 
    print("Null" if cur.next==None else cur.next.data)