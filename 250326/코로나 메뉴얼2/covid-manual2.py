arr=[]
for i in range(3):
    arr.append(list(input().split()))
type=[]
def check(p):
    if int(p[1])>=37:
        if p[0]=="Y":
            return("A")
        else:
            return("B")
    else:
        if p[0]=="Y":
            return("C")
        else:
            return("D")

for p in arr:
    type.append(check(p))
ch=[chr(ord("A")+i) for i in range(4)]
for c in ch:
    print(type.count(c),end=" ")
if type.count("A")>=2:
    print("E")

