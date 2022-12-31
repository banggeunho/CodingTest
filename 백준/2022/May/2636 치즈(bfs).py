from collections import deque
m, n = map(int, input().split())
data = []
for i in range(m):
    data.append(list(map(int, input().split())))


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def removeCheese(arr):
    cnt = 0
    for i in range(m):
        for j in range(n):
            if arr[i][j] == 2:
                arr[i][j] = 0
                cnt += 1
    return cnt

def printMap(arr):
    for i in range(m):
        for j in range(n):
            print(arr[i][j], end=' ')
        print()
    print()

def checkComplete(arr):
    for i in range(m):
        for j in range(n):
            if arr[i][j] == 1 or arr[i][j] == 2:
                return False

    return True

def bfs(i, j):
    visited = [[False] * n for _ in range(m)]
    q = deque()
    q.append((i, j))
    visited[i][j] = True

    while q:
        # print(q)
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                if data[nx][ny] == 0:
                    q.append((nx, ny))
                else:
                    data[nx][ny] = 2
                visited[nx][ny] = True
time = 0
before_cheese = 0
while True:
    before_cheese = removeCheese(data)
    if checkComplete(data):
        break
    bfs(0, 0)
    # printMap(data)
    time += 1

print(time)
print(before_cheese)
