N,B=map(int,input().split())
students=[
    list(map(int,input().split()))
    for _ in range(N)
]

students=[[p,s,p+s] for p,s in students]
available=[]
for i in range(N):
    students[i][0]//=2
    students[i][2]=students[i][0]+students[i][1]
    bs=[x[2] for x in students]
    tot=0
    max_students=0
    for j in range(N):
        min_index=bs.index(min(bs))
        b_trash=max(bs)+1
        if tot+students[min_index][2]>B:
            break
        else:
            tot+=students[min_index][2]
            max_students+=1
            bs[min_index]=b_trash
    available.append(max_students)
    students[i][0]*=2
    students[i][2]=students[i][0]+students[i][1]
print(max(available))