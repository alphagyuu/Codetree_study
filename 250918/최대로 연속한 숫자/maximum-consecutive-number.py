'''
(0,9) 9
(0,3) (4,9) 5
'''

from sortedcontainers import SortedSet

N,M=map(int,input().split())

seqs=SortedSet()
seqs.add((0,N+1))

lens=SortedSet()
lens.add((N+1,0,N+1))

ns=tuple(map(int,input().split()))

for n in ns:
    idx=seqs.bisect_right((n,N+2))
    a,b=seqs[idx-1]
    seqs.remove((a,b))
    lens.remove((b-a,a,b))
    if a!=n:
        seqs.add((a,n))
        lens.add((n-a,a,n))
    if b!=n+1:
        seqs.add((n+1,b))
        lens.add((b-n-1,n+1,b))
    print(lens[-1][0])