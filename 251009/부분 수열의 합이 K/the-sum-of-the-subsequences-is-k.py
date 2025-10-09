N,K = map(int,input().split())

ns = [0] + list(map(int,input().split()))

prefix_sums = [0,ns[1]]

for i in range(2,N+1):
    prefix_sums.append(prefix_sums[i-1] + ns[i])

cnt=0

for i in range(1,N+1):
    if prefix_sums[i]==K:
        cnt+=1
    elif prefix_sums[i]>K:
        for j in range(2,i):
            partial_sum=prefix_sums[i]-prefix_sums[j-1]
            if partial_sum==K:
                cnt+=1
                break

print(cnt)