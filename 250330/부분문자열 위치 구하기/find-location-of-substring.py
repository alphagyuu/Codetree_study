word=input()
part=input()

'''
pidx=0
yes=False
pos=0
for i in range(len(word)):
    if yes: 
        break
    if word[i]==part[pidx]:
        pidx+=1
        if pidx==len(part):
            yes=True
            pos=i-len(part)+1
    elif word[i]==part[0]:
        pidx=1
    else:
        pidx=0
if yes:
    print(pos)
else:
    print(-1)
'''
if part in word:
    print(word.index(part))
else:
    print(-1)