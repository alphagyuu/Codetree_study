arr=list(map(int,input().split(" ")))
def tot(arr):
    for i in range(len(arr)):
        if arr[i]>=250:
            return arr[0:i]
    return arr
cut=tot(arr)
total=sum(cut)
print(f"{total} {total/len(cut):.1f}")