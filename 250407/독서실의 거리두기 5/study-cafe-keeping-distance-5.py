N=int(input())
seats=input()
#print(seats)
seats=[seats[i] for i in range(len(seats))]

max_combo=0
for i in range(len(seats)):
    if seats[i]=="1":
        continue
    else:
        seats[i]="1"
    combo=0
    #print(seats)
    min_combo=len(seats)
    for j in range(len(seats)):
        if seats[j]=='0':
            combo+=1
        else:
            if combo==0:
                if j>0:
                    min_combo=0
            elif min_combo>combo:
                min_combo=combo
            combo=0
    if min_combo>max_combo:
        max_combo=min_combo
    seats[i]="0"
print(max_combo+1)