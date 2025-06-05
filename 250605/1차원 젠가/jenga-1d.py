N=int(input())
blocks=[int(input()) for _ in range(N)]
for _ in range(2):
    s,e=map(int,input().split())
    blocks=blocks[:s-1]+blocks[e:]
print(len(blocks))
for b in blocks:
    print(b)