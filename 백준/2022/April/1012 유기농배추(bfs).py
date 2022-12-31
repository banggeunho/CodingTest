# 구역 나누기 bfs 문제
# 방문 list를 활용하여 풀면된다.
from collections import deque
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


for tc in range(int(input())):
    q = deque()
    m, n, k = map(int, input().split())
    arr = [[0] * n for _ in range(m)]
    visited = [[False] * n for _ in range(m)]
    # print(arr)

    for i in range(k):
        a, b = map(int, input().split())
        arr[a][b] = 1

    def bfs(x, y):
        global q, visited
        q.append((x, y))
        visited[x][y] = True

        while q:
            cx, cy = q.popleft()
            for i in range(4):
                nx = cx + dx[i]
                ny = cy + dy[i]
                if 0 <= nx < m and 0 <= ny < n:
                    if arr[cx][cy] == arr[nx][ny] and not visited[nx][ny]:
                        q.append((nx, ny))
                        visited[nx][ny] = True

    result = 0
    # 전체 map을 보면서 방문하지 않았으면서 배추가 심어져있으면 새로운 구역으로 간주
    for i in range(m):
        for j in range(n):
            if not visited[i][j] and arr[i][j] == 1:
                bfs(i, j)
                result += 1

    print(result)