'''
123 -> 0
12 4 -> 1
1 3 5 -> 2
거리차이
1 1
1 큼
큼 큼
'''
humans=list(map(int,input().split()))
d1=humans[1]-humans[0]
d2=humans[2]-humans[1]
if d2>1 and d1>1:
    print(2)
elif d1==1 and d2==1:
    print(0)
else:
    print(1)
