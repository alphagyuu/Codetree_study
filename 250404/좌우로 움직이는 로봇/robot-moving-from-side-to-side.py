ln, lm = map(int, input().split())

amove = [input().split() for _ in range(ln)]
bmove = [input().split() for _ in range(lm)]

amove = [[int(t), d] for t, d in amove]
bmove = [[int(t), d] for t, d in bmove]

apos = bpos = 0
amp = bmp = 0
count = 0

# 각 명령 남은 시간 및 방향
atime, adir = amove[0]
btime, bdir = bmove[0]

while True:
    # A 움직임
    if adir is not None:
        apos += 1 if adir == "R" else -1
        atime -= 1

    # B 움직임
    if bdir is not None:
        bpos += 1 if bdir == "R" else -1
        btime -= 1

    # 충돌 체크
    if apos == bpos and adir != bdir:
        count += 1

    # A 다음 명령 처리
    if adir is not None and atime == 0:
        amp += 1
        if amp < ln:
            atime, adir = amove[amp]
        else:
            adir = None  # 멈춘 상태

    # B 다음 명령 처리
    if bdir is not None and btime == 0:
        bmp += 1
        if bmp < lm:
            btime, bdir = bmove[bmp]
        else:
            bdir = None  # 멈춘 상태

    # 종료 조건
    if adir is None and bdir is None:
        break

print(count)
