class Account:
    def __init__(self,i="codetree",l=10):
        self.i=str(i)
        self.l=int(l)
    def out(self):
        print(f"user {self.i} lv {self.l}")

a=Account()
b=Account(*input().split())

a.out()
b.out()