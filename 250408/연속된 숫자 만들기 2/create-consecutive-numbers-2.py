'''
123 -> 0
12 4 -> 1
1 3 5 -> 1
1 2 6 -> 2
거리차이 set
1 1 -> 0
1 2 -> 1
1 3보다큼 -> 2 
2 2 -> 1
2 3 -> 1
...
3 3 -> 2
'''
humans=list(map(int,input().split()))
d1=humans[1]-humans[0]
d2=humans[2]-humans[1]
if d2==2 or d1==2:
    print(1)
elif d1==1 and d2==1:
    print(0)
else:
    print(2)
