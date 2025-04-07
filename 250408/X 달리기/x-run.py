X=int(input())
'''
1               1~3 
1 2 1   4       4~8 어쩔수 없이 2가 max.
ex 7: 1 2 2 1 1
1 2 (3 2) 1   9
1 2 3 (4 3) 2 1
1 2 3 4 (5 4) 3 2 1
'''
stepnums=1
step_top=1
while stepnums+step_top*2+1<=X:
    stepnums+=(step_top*2+1)
    step_top+=1

#print(stepnums,step_top)

time_taken=step_top*2-1
X-=stepnums
while X>0:
    if X>=step_top:
        X-=step_top
        time_taken+=1
    else:
        step_top-=1
print(time_taken)
