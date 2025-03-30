slist=[
    str(input()) for j in range(3)
]
lenlist=[
    len(s) for s in slist
]
print(max(lenlist)-min(lenlist))