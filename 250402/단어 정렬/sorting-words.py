ln=int(input())
words=[
    input()
    for _ in range(ln)
]
words.sort()
for word in words:
    print(word)