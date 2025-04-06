x,y=map(int,input().split())

max_hap=0
for i in range(x,y+1):
    s=str(i)
    hap=0
    for j in range(len(s)):
        hap+=int(s[j])
    if hap>max_hap:
        max_hap=hap
print(max_hap)