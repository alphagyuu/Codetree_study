N,S = map(int,input().split())

ns = tuple(map(int,input().split()))

j = 0
tot = 0
min_length = N
for i in range(N):
    while j+1<N and tot<S:
        tot+=ns[j]
        j+=1
    if tot>=S:
        min_length = min(min_length,j-i)
        tot-=ns[i]

print(min_length)