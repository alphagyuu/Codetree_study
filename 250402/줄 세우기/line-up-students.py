ln=int(input())
students=[
    list(map(int,input().split())) + [i+1]
    for i in range(ln)
]
students.sort(key=lambda s:(s[0],s[1],-s[2]),reverse=True)
for s in students:
    print(s[0],s[1],s[2])