import copy
from collections import deque

INF = float('inf')
n, m = map(int, input().split())
arr = [list(map(int, input())) for _ in range(n)]
visited = [[INF] * m for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(visited):
    q = deque()
    q.append((0, 0))
    visited[0][0] = 1

    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not arr[nx][ny]:
                if visited[cx][cy] + 1 < visited[nx][ny]:
                    q.append((nx, ny))
                    visited[nx][ny] = visited[cx][cy] + 1

result = 2000
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            tmp_visited = copy.deepcopy(visited)
            arr[i][j] = 0
            bfs(tmp_visited)
            if tmp_visited[n-1][m-1]:
                result = min(result, tmp_visited[n-1][m-1])
            arr[i][j] = 1

if result == 2000:
    print(-1)
else:
    print(result)