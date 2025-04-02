states=["e","w","b","g"]
ln=int(input())
insts=[tuple(map(str,input().split())) for _ in range(ln)]
insts=[[int(x),d] for x,d in insts]
#print(insts)

front=-sum(x for [x,d] in insts if d=="L")
back=sum(x for [x,d] in insts if d=="R")
axis=["e"]*(back-front+1)

def R(s):
    if s=="e":
        return "b"
    elif s=="g":
        return "g"
    elif s.count("b")>=1 and s.count("w")>=2:
        return "g"
    else: 
        s+="b"
        return s
    
def L(s):
    if s=="e":
        return "w"
    elif s=="g":
        return "g"
    elif s.count("b")>=2 and s.count("w")>=1:
        return "g"
    else: 
        s+="w"
        return s


pos=-front
for inst in insts:
    if inst[1]=="R":
        axis[pos:pos+inst[0]]=[str(R(c)) for c in axis[pos:pos+inst[0]]]
        pos=pos+inst[0]-1
        
    else:
        axis[pos-inst[0]+1:pos+1]=[str(L(c)) for c in axis[pos-inst[0]+1:pos+1]]
        pos=pos-inst[0]+1

final=[x[-1] for x in axis]
#print(axis)

print(final.count("w"),final.count("b"),final.count("g"))
