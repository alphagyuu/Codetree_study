N=int(input())
rooms=[int(input()) for _ in range(N)]


moves=[]
for i in range(N):
    tot=0
    for j in range(N):
        tot+=rooms[j]*((j-i)%N)
    moves.append(tot)
print(min(moves))