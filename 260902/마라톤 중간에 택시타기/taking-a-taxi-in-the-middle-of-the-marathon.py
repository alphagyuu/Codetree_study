n = int(input())

cps = [tuple(map(int,input().split())) for _ in range(n)]

dis = [abs(cps[i][1]-cps[i-1][1])+abs(cps[i][0]-cps[i-1][0]) for i in range(1,n)]

gain = 0
for i in range(n-2):
    gain = max(gain, dis[i]+dis[i+1]-(abs(cps[i+2][0]-cps[i][0])+abs(cps[i+2][1]-cps[i][1])))

print(sum(dis) - gain)