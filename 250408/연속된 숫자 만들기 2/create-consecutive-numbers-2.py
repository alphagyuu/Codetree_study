'''
123 -> 0
12 4 -> 1
1 3 5 -> 2
거리차이 set
1 1 -> 0
1 2
2 2 하나라도 2이하이면 -> 1
'''
humans=list(map(int,input().split()))
d1=humans[1]-humans[0]
d2=humans[2]-humans[1]
if d2==1 and d1==1:
    print(0)
elif d1<=2 or d2<=2:
    print(1)
else:
    print(2)
