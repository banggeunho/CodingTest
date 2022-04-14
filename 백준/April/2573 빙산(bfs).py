# 빙산 줄이는 조건과 빙산의 구역을 체크하는 조건을 각자 걸어주는게 포인트

from collections import deque
n, m = map(int, input().split())
arr = []
visited = [[False]*m for _ in range(n)]
for i in range(n):
    data = list(map(int, input().split()))
    arr.append(data)

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(x, y):
    global visited, check_visited
    q = deque()
    q.append((x, y))

    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if arr[x][y] == 0 and arr[nx][ny] != 0:
                    arr[nx][ny] -= 1
                    if arr[nx][ny] == 0:
                        visited[nx][ny] = True

                elif arr[x][y] == 0 and arr[nx][ny] == 0 and not visited[nx][ny]:
                    q.append((nx, ny))
                    visited[nx][ny] = True

                elif arr[x][y] != 0 and arr[nx][ny] != 0 and not check_visited[nx][ny]:
                    q.append((nx, ny))
                    check_visited[nx][ny] = True

count = 0
time = 0
while count < 2:
    count = 0
    time += 1
    visited = [[False]*m for _ in range(n)]
    check_visited = [[False]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0 and not visited[i][j]:
                visited[i][j] = True
                bfs(i, j)

    for i in range(n):
        for j in range(m):
            if arr[i][j] != 0 and not check_visited[i][j]:
                check_visited[i][j] = True
                bfs(i, j)
                count += 1
                if count == 2:
                    break

    if count == 0:
        time = 0
        break

print(time)