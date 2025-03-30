s_,q_=map(str,input().split())
sl=list(s_)
q=int(q_)
qlist=[]
for i in range(q):
    qin_=list(map(str,input().split()))
    if qin_[0]=="1":
        qlist.append([1,int(qin_[1]),int(qin_[2])])
    else:
        qlist.append([2,qin_[1],qin_[2]])
for que in qlist:
    if que[0]==1:
        sl[que[1]-1],sl[que[2]-1]=sl[que[2]-1],sl[que[1]-1]
    else:
        sl=list(("".join(sl)).replace(que[1],que[2]))
    print("".join(sl))
