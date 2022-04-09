# 백준 2468번 안전영역
# https://www.acmicpc.net/problem/2468
from collections import deque
n = int(input())
arr = []
visited = [[False]*n for i in range(n)]
for i in range(n):
    arr.append(list(map(int, input().split())))

# 상하좌우를 살펴보기 위한 변수
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(x, y, k):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    while q: # 상하좌우 보겠다.
        cx, cy = q.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < n and 0 <= ny < n: # 범위를 벗어나지 않거나, 설정한 지점보다 높거나, 방문한 적이 없다면
                if arr[nx][ny] > k and not visited[nx][ny]:
                    q.append((nx, ny))
                    visited[nx][ny] = True

result = 0
for k in range(100): # 장마의 높이는 1부터 100까지
    cnt = 0
    visited = [[False]*n for _ in range(n)] # 방문노드 초기화
    for i in range(n): # 구역 카운트 시작!!
        for j in range(n):
            if arr[i][j] > k and not visited[i][j]:
                bfs(i, j, k)
                cnt += 1
    # 구역 갯수 갱신
    result = max(result, cnt)

print(result)
