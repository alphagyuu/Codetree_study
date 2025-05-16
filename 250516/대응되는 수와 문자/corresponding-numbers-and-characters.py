N,M=map(int,input().split())
c2n=dict()
n2c=dict()

for i in range(N):
    turn=str(i+1)
    ch=input()
    c2n[ch]=turn
    n2c[turn]=ch

for _ in range(M):
    x=input()
    if x in c2n:
        print(c2n[x])
    else:
        print(n2c[x])
