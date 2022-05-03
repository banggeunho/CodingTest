# 순환시키는 부분 함수 구현하는게 포인트...............................
# 확산할때도 이전의 값을 유지해서 확산하는게 포인트........................
# 어렵다.................................
r, c, t = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(r)]

up = -1
down = -1
# 공기 청정기 위치 찾기
for i in range(r):
    if arr[i][0] == -1:
        up = i
        down = i + 1
        break

# 확산
def spreading(x, y, k):
    dx = [0, 0, -1, 1]  # 좌, 우, 상, 하
    dy = [-1, 1, 0, 0]  # 0, 1, 2, 3
    cnt = 0
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < r and 0 <= ny < c and arr[nx][ny] > -1:
            arr[nx][ny] += k // 5
            cnt += 1

    if cnt > 0:
        arr[x][y] -= (k // 5) * cnt


def getLocation(arr):
    locations = []
    for i in range(r):
        for j in range(c):
            if arr[i][j] > 0:
                locations.append((i, j, arr[i][j]))

    return locations

# 공기청정기 위쪽 이동
def air_up():
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    direct = 0
    before = 0
    x, y = up, 1
    while True:
        nx = x + dx[direct]
        ny = y + dy[direct]
        if x == up and y == 0:
            break
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            direct += 1
            continue
        arr[x][y], before = before, arr[x][y]
        x = nx
        y = ny

# 공기청정기 아래쪽 이동
def air_down():
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    direct = 0
    before = 0
    x, y = down, 1
    while True:
        nx = x + dx[direct]
        ny = y + dy[direct]
        if x == down and y == 0:
            break
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            direct += 1
            continue
        arr[x][y], before = before, arr[x][y]
        x = nx
        y = ny



for _ in range(t):
    locations = getLocation(arr)
    for i, j, k in locations:
        spreading(i, j, k)
    air_up()
    air_down()

answer = 0
for i in range(r):
    for j in range(c):
        if arr[i][j] > 0:
            answer += arr[i][j]

print(answer)