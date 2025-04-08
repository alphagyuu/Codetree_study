n=int(input())
answer=[]
#answers=[]
tot=0
def choose(cur):
    global tot
    if cur>=n:
        if cur==n:
            if len(answer)>0:
                #print(answer)
                tot+=1
        return
    for i in range(1,5):
        answer.append(i)
        choose(cur+i)
        answer.pop()

choose(0)
print(tot)
#print(answers)
    