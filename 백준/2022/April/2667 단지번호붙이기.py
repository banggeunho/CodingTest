# very easy
# 각자의 구분을 구별하는 bfs 문제
# 단지의 수를 구하는 것은 큐에서 pop된 갯수를 세면 된다.

from collections import deque
n = int(input())

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
arr = []
for i in range(n):
    arr.append(list(map(int, input())))

visited = [[False]* n for _ in range(n)]

def bfs(a, b):
    q = deque()
    q.append((a, b)) # x, y, cost
    visited[a][b] = True
    # arr[a][b] = count
    cnt = 0

    while q:
        x, y = q.popleft()
        cnt += 1
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and arr[nx][ny] == 1:
                q.append((nx, ny))
                visited[nx][ny] = True
                # arr[nx][ny] = count

    return cnt

count = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1 and not visited[i][j]:
            count.append(bfs(i, j))

print(len(count))
for i in sorted(count):
    print(i)