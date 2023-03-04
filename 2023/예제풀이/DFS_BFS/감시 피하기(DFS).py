import itertools

arr = []
x_pos = []
solve = True
n = int(input())
for i in range(n):
    arr.append(list(input().split()))
    for j in range(n):
        if arr[i][j] == 'X':
            x_pos.append((i, j))

candidates = itertools.combinations(x_pos, 3)

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def dfs(x, y, arr):
    global dx, dy, n
    # 4 방향 검사
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue

        # 학생을 찾은 경우
        if arr[nx][ny] == 'S':
            return False

        # 장애물이 있는 경우
        if arr[nx][ny] == 'O':
            continue

        # 일반 복도인 경우
        if arr[nx][ny] == 'X':
            while True:
                nx += dx[i]
                ny += dy[i]

                # 지도 범위에 벗어 날 경우
                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    break

                # 장애물이 존재할 경우
                if arr[nx][ny] == 'O':
                    break

                # 학생을 찾은 경우
                if arr[nx][ny] == 'S':
                    return False

    return True


for candidate in candidates:
    solve = True
    # 경우에 따라 지도 설정
    for x, y in candidate:
        arr[x][y] = 'O'

    for i in range(n):
        for j in range(n):
            if arr[i][j] == 'T' and solve:
                solve = dfs(i, j, arr)

    if solve:
        print('YES')
        break

    # 지도 설정 복원
    for x, y in candidate:
        arr[x][y] = 'X'

if not solve:
    print('NO')