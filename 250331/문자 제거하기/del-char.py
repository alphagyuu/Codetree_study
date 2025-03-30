word=input()
for i in range(len(word)-1):
    n=int(input())
    if n>=len(word):
        word=word[:-1]
    else:   
        word=word[:n]+word[n+1:]
    print(word)