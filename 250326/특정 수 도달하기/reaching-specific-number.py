arr=list(map(int,input().split(" ")))
def tot(arr):
    total=0
    i=0
    for a in arr:
        if a<250:
            total+=a
            i+=1
        else:
            break
    return(f"{total} {total/i:.1f}")
print(tot(arr))