ln=int(input())
nums=list(map(int,input().split()))
def f(l):
    print(*[x if x%2==1 else x//2 for x in l])
f(nums[:])