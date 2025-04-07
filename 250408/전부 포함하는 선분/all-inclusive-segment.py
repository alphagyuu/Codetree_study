"""
1 5 
4 6
15 23
7 10
2 4

단 하나만 제거.
-> 최소 or 최대 인거 두개만 검사.

틀린이유

여기서 
1 5 
4 6
15 23
7 10
2 4
1 6

있어도 1 5 제거하든, 1 6 제거하든 똑같음.
더 중요한건 제거했을때 **그 다음 순위와의 차이.**
"""

N=int(input())
lines=[
    list(map(int,input().split()))
    for _ in range(N)
]

x1s=[x1 for x1,_ in lines]
x2s=[x2 for _,x2 in lines]


fronti=x1s.index(min(x1s))
backi=x2s.index(max(x2s))

x1s.sort()
x2s.sort()

if x1s[1]-x1s[0]>x2s[-1]-x2s[-2]:
    lines.pop(fronti)
    #앞쪽 제거
else:
    lines.pop(backi)



x1s=[x1 for x1,_ in lines]
x2s=[x2 for _,x2 in lines]

print(max(x2s)-min(x1s))


