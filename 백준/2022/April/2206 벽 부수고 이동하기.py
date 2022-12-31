# 벽을 부순 경로와 부수지 않은 경로를 따로 생각하여 문제 풀이
from collections import deque
n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input())))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
visited = [[[0]*2 for _ in range(m)] for _ in range(n)]

def bfs():
    q = deque()
    q.append((0, 0, 1))
    visited[0][0][1] = 1
    while q:
        x, y, w = q.popleft()
        if x == n - 1 and y == m - 1:
            return visited[x][y][w]

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] == 1 and w == 1: # w가 1이면 벽을 부시지 않은 상태
                    visited[nx][ny][0] = visited[x][y][1] + 1
                    q.append((nx, ny, 0))
                elif arr[nx][ny] == 0 and visited[nx][ny][w] == 0:
                    visited[nx][ny][w] = visited[x][y][w] + 1
                    q.append((nx, ny, w))

    return -1
print(bfs())