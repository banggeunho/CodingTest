from collections import deque

N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]



def bfs(start, visited):
    x, y = start
    q = deque()
    q.append((x, y))
    visited[x][y] = True

    total, count, union_idx = 0, 0, []
    while q:
        cx, cy = q.popleft()

        total += arr[cx][cy]
        count += 1
        union_idx.append((cx, cy))

        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if L <= abs(arr[cx][cy] - arr[nx][ny]) <= R:
                    q.append((nx, ny))
                    visited[nx][ny] = True

    return total, count, union_idx

result = 0
while True:
    moved = False
    visited = [[False] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                total, count, union_idx = bfs((i, j), visited)

                if count > 1:
                    moved = True
                    for x, y in union_idx:
                        arr[x][y] = int(total/count)

    if not moved:
        break

    else:
        result += 1

print(result)