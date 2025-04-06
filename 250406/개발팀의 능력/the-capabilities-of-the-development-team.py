devs=list(map(int,input().split()))

total=sum(devs)
min_diff=total
for i in range(5):
    for j in range(5):
        for k in range(5):
            if i==j or j==k or k==i:
                continue
            else:
                teama=devs[i]+devs[j]
                teamb=devs[k]
                teamc=total-teama-teamb
                if teama!=teamb and teamb!=teamc and teamc!=teama:
                    diff=max(teama,teamb,teamc)-min(teama,teamb,teamc)
                    if diff<min_diff:
                        min_diff=diff
if min_diff==total:
    print(-1)
else:
    print(min_diff)
            