ln_s,k_s,t=map(str,input().split())
ln,k=int(ln_s),int(k_s)
words=[
    input()
    for _ in range(ln)
]
dic=[x for x in words if x[0:len(t)]==t]
dic.sort()
print(dic[k-1])