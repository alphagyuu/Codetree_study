words=[]
while True:
    temp_w=str(input())
    if temp_w=="0":
        break
    else:
        words.append(temp_w)
print(len(words))
for i in range(len(words)):
    if i%2==0:
        print(words[i])
