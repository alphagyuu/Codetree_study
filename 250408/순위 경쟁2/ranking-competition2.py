'''
7
A -1    B
B 1
A 1
A 1     A,B
B 2     B
B 1
A 4     A

-> 4
'''

N=int(input())
turns=[list(map(str,input().split())) for _ in range(N)]
turns=[[c,int(s)] for c,s in turns]
#print(turns)
ascore=0
bscore=0
hof=["A","B"]
cnt=0
for c,s in turns:
    if c=="A":
        ascore+=s
    else:
        bscore+=s
    if ascore==bscore:
        new_hof=["A","B"]
    elif ascore>bscore:
        new_hof=["A"]
    else:
        new_hof=["B"]
    if hof!=new_hof:
        cnt+=1
        hof=new_hof
print(cnt)