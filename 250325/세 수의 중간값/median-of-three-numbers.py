dic=dict(zip(list('abc'),map(int,input().split(" "))))
print(1 if dic['b']>dic['a'] and dic['b']<dic['c'] else 0)