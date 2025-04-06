devs=list(map(int,input().split()))
min_diff=sum(devs)
for i in range(6):
    for j in range(6):
        if i!=j:
            for k in range(6):
                if j!=k and i!=k:
                    for l in range(6):
                        if k!=l and j!=l and i!=l:
                            m,n=(set([0,1,2,3,4,5])-set([i,j,k,l]))
                            diff=max(devs[i]+devs[j],devs[k]+devs[l],devs[m]+devs[n])-min(devs[i]+devs[j],devs[k]+devs[l],devs[m]+devs[n])
                            if diff<min_diff:
                                min_diff=diff
print(min_diff)
