
# vertical 검사
def Check_Vertical(tc, arr):
    for i in range(4):
        x_cnt = 0
        o_cnt = 0
        t_cnt = 0
        for j in range(4):
            if arr[j][i] == 'X':
                x_cnt += 1

            elif arr[j][i] == 'O':
                o_cnt += 1

            elif arr[j][i] == 'T':
                t_cnt += 1

        if x_cnt + t_cnt == 4:
            print(f'#{tc} X won')
            return True

        elif o_cnt + t_cnt == 4:
            print(f'#{tc} O won')
            return True

    return False

# horizontal 검사
def Check_Horizontal(tc, arr):
    for i in range(4):
        x_cnt = 0
        o_cnt = 0
        t_cnt = 0
        for j in range(4):
            if arr[i][j] == 'X':
                x_cnt += 1

            elif arr[i][j] == 'O':
                o_cnt += 1

            elif arr[i][j] == 'T':
                t_cnt += 1

        if x_cnt + t_cnt == 4:
            print(f'#{tc} X won')
            return True

        elif o_cnt + t_cnt == 4:
            print(f'#{tc} O won')
            return True

    return False

# 킹각선 검사
def Check_Diagnol(tc, arr):
    x_cnt = 0
    o_cnt = 0
    t_cnt = 0
    for i in range(4):
        if arr[i][i] == 'X':
            x_cnt += 1

        elif arr[i][i] == 'O':
            o_cnt += 1

        elif arr[i][i] == 'T':
            t_cnt += 1

        if x_cnt + t_cnt == 4:
            print(f'#{tc} X won')
            return True

        elif o_cnt + t_cnt == 4:
            print(f'#{tc} O won')
            return True

    x_cnt = 0
    o_cnt = 0
    t_cnt = 0
    for i in range(3, -1, -1):
        if arr[i][3-i] == 'X':
            x_cnt += 1

        elif arr[i][3-i] == 'O':
            o_cnt += 1

        elif arr[i][3-i] == 'T':
            t_cnt += 1

        if x_cnt + t_cnt == 4:
            print(f'#{tc} X won')
            return True

        elif o_cnt + t_cnt == 4:
            print(f'#{tc} O won')
            return True

    return False

# 끝났는지 검사
def Check_Completed(tc, arr):
    for i in range(4):
        for j in range(4):
            if arr[i][j] == '.':
                print(f'#{tc} Game has not completed')
                return True

    print(f'#{tc} Draw')

for tc in range(1, int(input())+1):
    arr = []
    while True:
        data = list(input())
        if len(data) != 4:
            break
        arr.append(data)

    if not Check_Vertical(tc, arr):
        if not Check_Horizontal(tc, arr):
            if not Check_Diagnol(tc, arr):
                Check_Completed(tc, arr)

    # print(f'#{tc} {total}')


