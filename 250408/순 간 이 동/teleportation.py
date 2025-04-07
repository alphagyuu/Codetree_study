A,B,x,y=map(int,input().split())

print(min((abs(B-A)),(abs(B-x)+abs(A-y)),(abs(B-y)+abs(A-x))))