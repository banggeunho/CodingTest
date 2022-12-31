# BFS
# 색맹 처리 안하고 한 번 돌리고, 색맹 처리 하고 한 번 더 돌린다.
# 구역별로 나누는 법은 VISITED 리스트 만들어서~
from collections import deque
n = int(input())
result, result1 = 0, 0
arr = []
for i in range(n):
    arr.append(list(input()))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs(x, y):
    global visited, arr
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    while q:
        x, y= q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if not visited [nx][ny]:
                    if arr[x][y] == arr[nx][ny]:
                        q.append((nx, ny))
                        visited[nx][ny] = True

# BFS
visited = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j)
            result += 1 # 구역별 카운트 1

# 색맹 처리
for i in range(n):
    for j in range(n):
        if arr[i][j] == 'R':
            arr[i][j] = 'G'

# 다시 BFS
visited = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j)
            result1 += 1

print(result, result1)