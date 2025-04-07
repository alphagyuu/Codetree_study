"""
1 5 
4 6
15 23
7 10
2 4

단 하나만 제거.
-> 최소 or 최대 인거 두개만 검사.
"""

N=int(input())
lines=[
    list(map(int,input().split()))
    for _ in range(N)
]

x1s=[x1 for x1,_ in lines]
x2s=[x2 for _,x2 in lines]

frontx=min(x1s)
backx=max(x2s)

maxdel=0
delidx=0
for i in range(len(lines)):
    length=0
    if lines[i][0]==frontx:
        length=lines[i][1]-frontx
    if lines[i][1]==backx:
        length=backx-lines[i][0]
    if maxdel<length:
        maxdel=length
        delidx=i
lines.pop(delidx)

x1s=[x1 for x1,_ in lines]
x2s=[x2 for _,x2 in lines]

print(max(x2s)-min(x1s))


