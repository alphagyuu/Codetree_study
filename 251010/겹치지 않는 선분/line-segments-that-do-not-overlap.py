from sortedcontainers import SortedSet

N = int(input())

lines = [tuple(map(int,input().split())) for _ in range(N)]

starts=SortedSet()
s2i = dict()
ends=SortedSet()
e2i = dict()

for i in range(N):
    s,e = lines[i]
    starts.add(s)
    s2i[s] = i
    ends.add(-e)
    e2i[e] = i

cnt_arr = [1]*N

for i in range(N):
    s,e = lines[i]
    s_f = starts.bisect_right(s)
    s_l = starts.bisect_right(e)
    e_f = ends.bisect_right(-e)
    e_l = ends.bisect_right(-s)
    sset = set()
    eset = set()
    for js in range(s_f,s_l):
        sset.add(s2i[starts[js]])
    for je in range(e_f,e_l):
        eset.add(e2i[-ends[je]])
    #print(s,e)
    #print(s_f,s_l,e_f,e_l)
    #print(sset, eset)
    for si in sset:
        if si in eset:
            cnt_arr[si] = 0
            cnt_arr[i] = 0

print(sum(cnt_arr))