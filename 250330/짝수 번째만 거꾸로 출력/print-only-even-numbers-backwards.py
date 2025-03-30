word=input()
for i in range(len(word)//2):
    if len(word)%2==0: 
        x=-(i+1)*2+1
    else:
        x=-(i+1)*2
    print(word[x],end="")