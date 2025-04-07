N=int(input())
word=input()
def loop(N,word):
    for i in range(N):
        parts=[]
        for j in range(len(word)-i):
            parts.append(word[j:j+i+1])
        if len(set(parts))==len(word)-i:
            return i+1
print(loop(N,word))