# 간단 간단
from collections import deque
n, m = map(int, input().split())

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

arr = []
for i in range(n):
    arr.append(list(map(int, input())))

visited = [[False]* m for _ in range(n)]

q = deque()
q.append((0, 0, 1)) # x, y, cost
visited[0][0] = True
result = int(1e9)
while q:
    x, y, cost = q.popleft()

    if x == n-1 and y == m-1:
        result = min(result, cost)

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and arr[nx][ny] == 1:
            q.append((nx, ny, cost+1))
            visited[nx][ny] = True

print(result)