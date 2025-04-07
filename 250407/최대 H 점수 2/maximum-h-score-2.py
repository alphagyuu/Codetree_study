N,L = map(int,input().split())
nums=list(map(int,input().split()))
nums.sort()
#print(nums)

#최소~최대, +1 모두 검사. 각 값-1보다 크거나 같은 수 개수가 ~이상인지.
maxh=0
for n in range(min(nums),max(nums)+1):
    for i in range(2):
        cnt_h=0
        cnt_h_1=0
        h=n+i #h에도 1 증가 가능.
        h_possible=0
        for nn in nums:
            if nn>=h: #h보다 크면
                cnt_h+=1
            elif nn>=h-1: #h-1이면
                cnt_h_1+=1
        if cnt_h>=h:
            h_possible=h
        elif cnt_h_1<=L and cnt_h_1+cnt_h>=h: #h-1을 h로 증ㅇ가시킨 경우가 L번보다 적어야함.
            h_possible=h
        if h_possible>maxh:
            maxh=h_possible
        #print(h,cnt_h,cnt_h_1)
        if L==0:
            break
print(maxh)
        