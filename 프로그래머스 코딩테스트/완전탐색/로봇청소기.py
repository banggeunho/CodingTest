# https://www.acmicpc.net/problem/14503
n, m = map(int, input().split())
cx, cy, direction = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]

answer = 0
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turnDriection(direction):
    return (direction - 1) % 4

def isCleanAround(x, y):
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and data[nx][ny] == 0:
            return False
    return True

def isWall(x, y):
    return 0 <= x < n and 0 <= y < m and data[x][y] == 1

def isNotClean(x, y):
    return 0 <= x < n and 0 <= y < m and data[x][y] == 0

while True:
    if data[cx][cy] == 0:
        data[cx][cy] = -1
        answer += 1

    if isCleanAround(cx, cy):
        nx, ny = cx - dx[direction], cy - dy[direction]
        if isWall(nx, ny):
            break
        else:
            cx, cy = nx, ny
            continue
    else:
        direction = turnDriection(direction)
        nx, ny = cx + dx[direction], cy + dy[direction]
        if isNotClean(nx, ny):
            cx, cy = nx, ny
        continue

print(answer)



