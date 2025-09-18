from sortedcontainers import SortedSet

s=SortedSet()

def main():
    N = int(input())
    for _ in range(N):
        p,l=map(int,input().split())
        s.add((l,p))
    M = int(input())
    for _ in range(M):
        inst=input().split()
        c=inst[0]
        if c=="rc":
            x=int(inst[1])
            if x==1:
                print(s[-1][1])
            else:
                print(s[0][1])
        else:
            p,l=map(int,inst[1:])
            if c=="ad":
                s.add((l,p))
            else:
                s.remove((l,p))


main()