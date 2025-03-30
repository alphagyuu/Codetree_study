a=input()
b=input()
cnt=0
pidx=0
for i in range(len(a)-len(b)+1):
    if a[i:i+len(b)]==b:
        cnt+=1
print(cnt)


