game=[
    input()
    for _ in range(3)
]

games=[[x[0],x[1],x[2]] for x in game]
teams=[]
#가로
for i in range(3):
    t=list(set(games[i]))
    if len(t)==2:
        t.sort()
        if t not in teams:
            teams.append(t)

for j in range(3):
    t=[]
    for i in range(3):
        t.append(games[i][j])
    t=list(set(t))
    if len(t)==2:
        t.sort()
        if t not in teams:
            teams.append(t)
t=[]
for i in range(3):
    t.append(games[i][i])
t=list(set(t))
if len(t)==2:
    t.sort()
    if t not in teams:
        teams.append(t)

t=[]
for i in range(3):
    t.append(games[2-i][i])
t=list(set(t))
if len(t)==2:
    t.sort()
    if t not in teams:
        teams.append(t)

print(len(teams))
        