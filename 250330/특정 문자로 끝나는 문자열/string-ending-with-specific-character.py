ln=int(input())
words=[
    input()
    for i in range(ln)
]
a=input()
pos=[]
for word in words:
    if word[0]==a:
        pos.append(len(word))
print(f"{len(pos)} {sum(pos)/len(pos):.2f}")