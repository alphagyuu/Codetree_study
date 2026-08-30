pan = [list(map(int,input().split())) for _ in range(19)]

def in_pan(i,j):
    return 0 <= i < 19 and 0 <= j < 19

def main():

    # 가로 →
    for i in range(19):
        combo = 0
        prev = 0

        for j in range(19):
            if pan[i][j] == 0 or prev != pan[i][j]:
                combo = 0

            combo += 1
            prev = pan[i][j]

            if combo == 5:
                print(prev)
                print(i+1, j-1)
                return

    # 세로 ↓
    for j in range(19):
        combo = 0
        prev = 0

        for i in range(19):
            if pan[i][j] == 0 or prev != pan[i][j]:
                combo = 0

            combo += 1
            prev = pan[i][j]

            if combo == 5:
                print(prev)
                print(i-1, j+1)
                return

    # ↘ : 왼쪽 변에서 출발
    for i in range(19):
        j = 0
        combo = 0
        prev = 0

        while in_pan(i,j):
            if pan[i][j] == 0 or prev != pan[i][j]:
                combo = 0

            combo += 1
            prev = pan[i][j]

            if combo == 5:
                print(prev)
                print(i-1, j-1)
                return

            i += 1
            j += 1

    # ↘ : 위쪽 변에서 출발
    for j in range(19):
        i = 0
        combo = 0
        prev = 0

        while in_pan(i,j):
            if pan[i][j] == 0 or prev != pan[i][j]:
                combo = 0

            combo += 1
            prev = pan[i][j]

            if combo == 5:
                print(prev)
                print(i-1, j-1)
                return

            i += 1
            j += 1

    # ↙ : 오른쪽 변에서 출발
    for i in range(19):
        j = 18            # 여기 0 → 18
        combo = 0
        prev = 0

        while in_pan(i,j):
            if pan[i][j] == 0 or prev != pan[i][j]:
                combo = 0

            combo += 1
            prev = pan[i][j]

            if combo == 5:
                print(prev)
                print(i-1, j+3)     # 여기 j+1 → j+3
                return

            i += 1
            j -= 1

    # ↙ : 위쪽 변에서 출발
    for j in range(19):
        i = 0
        combo = 0
        prev = 0

        while in_pan(i,j):
            if pan[i][j] == 0 or prev != pan[i][j]:
                combo = 0

            combo += 1
            prev = pan[i][j]

            if combo == 5:
                print(prev)
                print(i-1, j+3)     # 여기도 j+3
                return

            i += 1
            j -= 1

    print(0)

main()