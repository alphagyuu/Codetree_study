ln=int(input())
arr=list(map(int,input().split()))
def f(arr):
    print(*[abs(x) for x in arr])
f(arr)