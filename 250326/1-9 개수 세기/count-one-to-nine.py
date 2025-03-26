l=int(input())
arr=list(map(int,input().split()))
for i in range(9):
    print(arr.count(i+1))