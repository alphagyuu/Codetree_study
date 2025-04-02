class Bond:
    def __init__(self,c,p,t):
        self.c = str(c)
        self.p = str(p)
        self.t = int(t)
    def out(self):
        print(f"secret code : {self.c}")
        print(f"meeting point : {self.p}")
        print(f"time : {self.t}")

bond=Bond(*input().split())

bond.out()