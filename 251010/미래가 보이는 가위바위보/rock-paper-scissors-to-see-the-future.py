from itertools import permutations

N = int(input())

Bs = ['X']+[input() for _ in range(N)]

Hs = [0]*(N+2)
Ss = [0]*(N+2)
Ps = [0]*(N+2)

H_l = [0]*(N+2)
H_r = [0]*(N+2)
S_l = [0]*(N+2)
S_r = [0]*(N+2)
P_l = [0]*(N+2)
P_r = [0]*(N+2)

for i in range(1,N+1):
    b = Bs[i]
    if b =='H':
        Ps[i] = 1
    elif b == 'S':
        Hs[i] = 1
    else:
        Ss[i] = 1

for i in range(1,N+1):
    H_l[i] = H_l[i-1] + Hs[i]
    S_l[i] = S_l[i-1] + Ss[i]
    P_l[i] = P_l[i-1] + Ps[i]
    ri = N+1-i
    H_r[ri] = H_r[ri+1] + Hs[ri]
    S_r[ri] = S_r[ri+1] + Ss[ri]
    P_r[ri] = P_r[ri+1] + Ps[ri]

#print(list(permutations((0,1,2),2)))

max_wins = 0

for i in range(0,N+1):
    lw=(H_l[i],S_l[i],P_l[i])
    rw=(H_r[i+1],S_r[i+1],P_r[i+1])
    for ls,rs in list(permutations((0,1,2),2)):
        max_wins = max(max_wins, lw[ls]+rw[rs])

print(max_wins)