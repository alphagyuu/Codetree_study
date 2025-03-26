n=int(input())
cnt=0
for i in range(n):
    m=i+1
    if m%2!=0 and m%3!=0 and m%5!=0:
        cnt+=1
print(cnt)