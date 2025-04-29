N=int(input())
wordcounts=dict()
for _ in range(N):
    word=input()
    if word in wordcounts:
        wordcounts[word]+=1
    else:
        wordcounts[word]=1
print(max(wordcounts.values()))
    