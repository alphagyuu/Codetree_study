ln=int(input())
students=[
    input().split()
    for _ in range(ln)
]
students.sort(key=lambda x:sum(list(map(int,x[1:]))))
for s in students:
    print(*s)