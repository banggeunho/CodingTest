# 익은 토마토를 큐에 먼저 다 집어 넣고, 꺼내면서 인접 토마토 검사
# 인접 토마토 검사할때 안 익은 새1끼 있으면 큐에 넣어주면서 하루 늘려줌
# 모든 토마토의 탐색이 끝났을때 안 익은 새1끼가 있는지 확인
import sys
from collections import deque
q = deque()
m, n= map(int, input().split())
arr = []
days = 0

# 토마토 상태 입력 받기
for i in range(n):
    data = list(map(int, sys.stdin.readline().split()))
    arr.append(data)
    for j in range(m):
        if data[j] == 1:
            q.append((i, j, 0))

# 상하좌우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

while q:
    x, y, days = q.popleft()
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 0:
            q.append((nx, ny, days+1)) # 하루씩 추가~
            arr[nx][ny] = 1

# 안 익은 토마토 있으면 -1 출력
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            print(-1)
            exit(0)

# 다 익었음 days 출력
print(days)