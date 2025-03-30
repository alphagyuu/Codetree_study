slist=[
    input() for i in range(10)
]
a=input()
check=0
for s in slist:
    if s[-1]==a:
        print(s)
        check+=1
if check==0:
    print("None")