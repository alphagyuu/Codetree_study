def function():
    N,M = map(int,input().split())

    A = tuple(map(int,input().split()))
    B = tuple(map(int,input().split()))

    cnt = 0
    j=-1
    for i in range(N):
        while i+j+1<N:
            j+=1
            if A[i+j]==B[cnt]:
                cnt+=1
            if cnt >= M:
                return "Yes"
        cnt=0
    return "No"

print(function())