word,n_=map(str,input().split())
ln=int(n_)
qlist=[
    int(input())
    for i in range(ln)
]
for q in qlist:
    if q==1:
        word=word[1:]+word[0]
    elif q==2:
        word=word[-1]+word[:-1]
    else:
        word=word[::-1]
    print(word)
