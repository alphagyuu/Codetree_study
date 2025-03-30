ln=int(input())
words=list(map(str,input().split()))
s="".join(words)
for i in range(len(s)//5+1):
    print(s[i*5:i*5+5])