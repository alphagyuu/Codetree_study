lng=int(input())
items=list(map(int,input().split()))
items.sort()
groups=[]
for i in range(lng):
    groups.append(items.pop(0)+items.pop())
print(max(groups))