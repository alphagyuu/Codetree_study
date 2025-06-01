S=int(input())
start=1
end=S
max_num=0

def tot(n):
    return n*(n+1) // 2

while start<=end:
    mid=(start+end)//2
    val=tot(mid)
    if val<=S:
        start=mid+1
        max_num=max(max_num,mid)
    else:
        end=mid-1

print(max_num)