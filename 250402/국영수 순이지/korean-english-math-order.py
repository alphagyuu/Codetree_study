class P:
    def __init__(self,name,k,e,m):
        self.name=str(name)
        self.k=str(k)
        self.e=str(e)
        self.m=str(m)
    def out(self):
        print(self.name,self.k,self.e,self.m)

ln=int(input())
people=[
    P(*input().split())
    for _ in range(ln)
]
people.sort(key=lambda x:(x.k+x.e+x.m),reverse=True)
for p in people:
    p.out()