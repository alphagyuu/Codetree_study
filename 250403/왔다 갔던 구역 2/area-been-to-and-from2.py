ln=int(input())
insts=[tuple(map(str,input().split())) for x in range(ln)]
insts=[[int(x),d] for x,d in insts]
mjs=[]
pos=0
def l(inst,pos):
    if inst[1]=="R":
        return(list(range(pos,inst[0]+pos)))
    else:
        return(list(range(pos-inst[0],pos)))
#print(l([2,"L"],0))
for inst in insts:
    mjs+=l(inst,pos)
    if inst[1]=="R":
        pos+=inst[0]
    else:
        pos-=inst[0]
mjs_set=set(mjs)
print(len(list(filter(lambda x:x>=2,[mjs.count(line) for line in mjs_set]))))
#print(sum(1 for line in mjs_set if mjs.count(line) >= 2))