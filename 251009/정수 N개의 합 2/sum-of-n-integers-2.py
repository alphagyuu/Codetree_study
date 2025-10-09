N,K=map(int,input().split())

ns=[0]+list(map(int,input().split()))

prefix_sum=[0,ns[1]]

for i in range(2,N+1):
    prefix_sum.append(prefix_sum[i-1]+ns[i])

#print(prefix_sum)

top_sum=0

for i in range(K,N+1):
    top_sum = max(top_sum, prefix_sum[i]-prefix_sum[i-K])

print(top_sum)