arr=[]
for i in range(5):
    arr.append(int(input()))
cnt=0
for a in arr:
    if a%2==0: cnt+=1
print(cnt)