word=input()
for i in range(len(word)+1):
    print(word)
    word=word[-1]+word[:-1]