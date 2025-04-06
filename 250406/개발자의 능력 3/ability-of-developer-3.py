devs=list(map(int,(input().split())))
def loop():
    tot=sum(devs)
    minimum=tot%2
    min_diff=tot
    for i in range(6):
        for j in range(i+1,6):
            for k in range(j+1,6):
                temp=devs[i]+devs[j]+devs[k]
                diff=abs(temp*2-tot)
                if diff==minimum:
                    return diff
                if diff<min_diff:
                    min_diff=diff
    return min_diff
print(loop())
    