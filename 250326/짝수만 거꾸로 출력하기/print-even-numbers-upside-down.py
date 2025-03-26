l=int(input())
arr=list(map(int,input().split()))
print(*[arr[-i-1] for i in range(l) if arr[-i-1]%2==0])