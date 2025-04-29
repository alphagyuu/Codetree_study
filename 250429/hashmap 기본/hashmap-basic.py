N=int(input())

insts=[
    list(map(str,input().split()))
    for _ in range(N)
]
hmap=dict()
for turn in range(N):
    cur_inst=insts[turn]
    #print(cur_inst)
    if cur_inst[0]=="add":
        hmap[cur_inst[1]]=cur_inst[2]
    elif cur_inst[0]=="remove":
        hmap.pop(cur_inst[1])
    elif cur_inst[0]=="find":
        print(hmap.get(cur_inst[1],"None"))
    else:
        break

