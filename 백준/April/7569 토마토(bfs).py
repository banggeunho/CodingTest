# 익은 토마토를 큐에 먼저 다 집어 넣고
# 익지 않은 토마토가 있으면 익은 걸로 바꿔주고, cost(day)를 1씩 추가
# 최종적으로 안 익은 토마토가 있으면 -1 출력 아니면 cost 출력
import sys
from collections import deque
q = deque()
m, n, h = map(int, input().split())
arr = [[] for _ in range(h)]

for i in range(h):
    for j in range(n):
        data = list(map(int, sys.stdin.readline().split()))
        arr[i].append(data)
        for k in range(m):
            if data[k] == 1:
                q.append((i, j, k, 0))


dx = [0, 0, 0, 0, -1, 1]
dy = [0, 0, -1, 1, 0, 0]
dh = [-1, 1, 0, 0, 0, 0]
cost = 0
while q:
    v, x, y, cost = q.popleft()
    for i in range(6):
        nx, ny, nh = x+dx[i], y+dy[i], v+dh[i]
        if 0 <= nx < n and 0 <= ny < m and 0 <= nh < h and arr[nh][nx][ny] == 0: # 범위 안에 있을때
            q.append((nh, nx, ny, cost+1))
            arr[nh][nx][ny] = 1

result = 0
for i in range(h):
    for j in range(n):
        for k in range(m):
            if arr[i][j][k] == 0:
                print(-1)
                exit(0)
print(cost)