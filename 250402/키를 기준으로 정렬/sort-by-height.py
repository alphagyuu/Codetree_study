class P:
    def __init__(self,name,h,w):
        self.name=str(name)
        self.h=int(h)
        self.w=int(w)
    def out(self):
        print(f"{self.name} {self.h} {self.w}")

ln=int(input())
people=[
    P(*input().split())
    for _ in range(ln)
]
people.sort(key=lambda x:x.h)
for p in people:
    p.out()