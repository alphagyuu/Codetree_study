N = int(input())

ns = tuple(map(int,input().split()))

cnts= [0]*(100001)

max_l = 0
j = 0

for i in range(N):
    while j<N and cnts[ns[j]] == 0:
        cnts[ns[j]]+=1
        j+=1
    cnts[ns[i]]-=1
    max_l = max(max_l,j-i)

print(max_l)