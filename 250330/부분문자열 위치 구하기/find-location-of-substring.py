word=input()
part=input()
pidx=0
yes=False
pos=0
for i in range(len(word)):
    if word[i]==part[pidx]:
        pidx+=1
        if pidx==len(part):
            yes=True
            pos=i-len(part)+1
            break
    else:
        pidx=0
if yes:
    print(pos)
else:
    print(-1)