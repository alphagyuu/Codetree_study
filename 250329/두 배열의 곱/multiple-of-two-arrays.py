arra=[
    list(map(int,input().split()))
    for _ in range(3)
]
input()
arrb=[
    list(map(int,input().split()))
    for _ in range(3)
]

for i in range(3):
    for j in range(3):
        arrb[i][j]=arra[i][j]*arrb[i][j]
    
for i in range(3):
    print(*arrb[i])
