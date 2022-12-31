from collections import deque
# 입력
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

# 8가지 방향
dx = [0, 0, 1, 1, 1, -1, -1, -1]
dy = [-1, 1, -1, 0, 1, -1, 0, 1]

def bfs(x, y):
    q = deque()
    visited = [[False]*m for _ in range(n)]
    q.append((x, y, 0))
    visited[x][y] = True

    while q:
        x, y, cost = q.popleft()
        if arr[x][y] == 1:
            return cost
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny, cost+1))

result = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            result = max(result, bfs(i, j))

print(result)