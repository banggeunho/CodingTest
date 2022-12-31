from collections import deque
while True:
    m, n = map(int, input().split())
    if m == 0 and n == 0:
        break
    arr = []
    visited = [[False]*m for _ in range(n)]
    for _ in range(n):
        arr.append(list(map(int, input().split())))

    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]

    def bfs(i, j):
        q = deque()
        q.append((i, j))
        visited[i][j] = True

        while q:
            x, y = q.popleft()
            for i in range(8):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and arr[nx][ny] == 1:
                    q.append((nx, ny))
                    visited[nx][ny] = True

    answer = 0
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and arr[i][j] == 1:
                bfs(i, j)
                answer += 1

    print(answer)