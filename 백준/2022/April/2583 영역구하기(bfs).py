# 입력 받는 부분이 살짝 골치 아팠지만 좌표계로 나타나 있어서
# 어떻게 값을 넣어줄까 생각해봤던 문제
# 하지만 주어진 값을 이용하면 반대로 입력된다 ( 좌표계랑 행렬의 인덱스는 반대이기 때문)
# 그러나 입력된 직사각형의 형태는 그대로 이므로 문제를 풀이하는 과정에서 전혀 문제가 안 된다 판단.

from collections import deque
m, n, k = map(int, input().split())
visited = [[False]*n for _ in range(m)]
arr = [[0]*n for _ in range(m)]
for _ in range(k):
    x, y, x1, y1 = map(int, input().split())
    for j in range(x, x1):
        for i in range(y, y1):
            arr[i][j] = 1

dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]

def bfs(x, y):
    cost = 0
    q = deque()
    q.append((x, y))
    visited[x][y] = True

    while q:
        cx, cy = q.popleft()
        cost += 1

        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and arr[nx][ny] == 0:
                q.append((nx, ny))
                visited[nx][ny] = True

    return cost

result = []
for i in range(m):
    for j in range(n):
        if not visited[i][j] and arr[i][j] == 0:
            result.append(bfs(i, j))

print(len(result))
for i in sorted(result):
    print(i, end =' ')
print()