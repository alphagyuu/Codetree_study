T = int(input())

dxdy = {'L': (-1,0), 'R': (1,0), 'U': (0,1), 'D': (0,-1)}

for _ in range(T):
    N = int(input())
    poss, ws, ds = [], [], []

    bi_removed = [False]*N
    for i in range(N):
        xi, yi, wi, di = input().split()
        poss.append((int(xi)*2,int(yi)*2))
        ws.append(int(wi))
        ds.append(di)
    latest = -1
    for time in range(4003):
        npos = dict()
        for i in range(N):
            if bi_removed[i]:
                continue
            x,y = poss[i]
            w = ws[i]
            d = ds[i]
            dx, dy = dxdy[d]
            nx, ny = x+dx, y+dy
            poss[i] = (nx,ny)
            if (nx,ny) in npos:
                ci = npos[(nx,ny)]
                latest = time+1
                if (w > ws[ci]) or (w == ws[ci] and i>ci):
                    bi_removed[ci] = True
                    npos[(nx,ny)] = i
                else:
                    bi_removed[i] = True
                    continue
            else:
                npos[(nx,ny)] = i

    print(latest)
            

        
            
