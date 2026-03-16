N = int(input())

left = 0
right = N*3 - 1

def cal(x):
    return x - x//3 - x//5 + x//15

while left <= right:
    mid = (left + right) // 2
    if tot >= N:
        tot = cal(mid)
        right = mid - 1
    else:
        left = mid + 1

print(mid)
