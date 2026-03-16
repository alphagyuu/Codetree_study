N = int(input())

ns = [] 



left = 0
right = N*3 - 1
cnt = 0

def cal(x):
    return x - x//3 - x//5 + x//15

while left <= right:
    mid = (left + right) // 2
    tot = cal(mid)
    if tot == N:
        break
    if tot < N:
        left = mid + 1
    else:
        right = mid - 1

print(mid)
