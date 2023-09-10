# https://www.acmicpc.net/problem/1261

from collections import deque
M, N = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input())))

visited = [[-1] * M for _ in range(N)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(start):
    x, y = start
    q = deque([(x, y)])
    visited[x][y] = 0

    while q:
        cx, cy = q.popleft()

        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if visited[nx][ny] == -1:
                    if arr[nx][ny] == 0:
                        visited[nx][ny] = visited[cx][cy]
                        q.appendleft((nx, ny))
                    else:
                        visited[nx][ny] = visited[cx][cy] + 1
                        q.append((nx, ny))

bfs((0, 0))
print(visited[N - 1][M - 1])