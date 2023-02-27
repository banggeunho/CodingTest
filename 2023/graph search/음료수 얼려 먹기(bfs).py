from collections import deque

n, m = map(int, input().split())

visited = [] # 얼음 정보 입력 받기
for i in range(n):
    visited.append(list(map(int, input())))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(start, visited):
    x, y = start
    q = deque()
    q.append((x, y))

    while q:
        cx, cy = q.popleft()
        print(cx, cy)
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0:
                q.append((nx, ny))
                visited[nx][ny] = 1

result = 0
for i in range(n):
    for j in range(m):
        if visited[i][j] == 0:
            visited[i][j] = 1
            bfs((i, j), visited)
            result += 1
            print('result', result)

print(result)