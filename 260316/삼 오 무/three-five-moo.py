N = int(input())

ns = [] 

for n in range(1, N*3):
    if n%3 == 0 or n%5 == 0:
        ns.append("Moo")
    else:
        ns.append(n)


left = 0
right = N*3 - 1
cnt = 0

def cal(l, r):
    cnt = 0
    for i in range(l,r):
        if ns[i] == "Moo":
            continue
        cnt += 1
    return cnt

while left <= right:
    mid = (left + right) // 2
    partial = cal(left, mid+1)
    if cnt + partial == N:
        cnt += partial
        break
    if cnt+partial < N:
        cnt += partial
        left = mid + 1
    else:
        right = mid - 1

print(ns[mid])
