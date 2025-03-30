a=input()
words=["apple","banana","grape","blueberry","orange"]
cnt=0
for word in words:
    if a==word[2] or a==word[3]:
        cnt+=1
        print(word)
print(cnt)