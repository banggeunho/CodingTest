# 이 문제는 구역을 나누는 문제가 아닌
# 각 구역에서 가장 거리 간 두 노드 사이의 최단 거리를 찾아야 하므로
# 각자 구역에 해당하는 위치에서 bfs를 수행하여 max값을 찾아내먄 된다.
# visited 함수를 bfs함수 안에서 구현해줌으로써 각 노드에서 매번 최단거리 경로를 찾게된다.
# 모든 노드에서 bfs를 수행하여 가장 긴 거리를 게속 최신화 해주면 정답을 구할 수 있음

from collections import deque
n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs(x, y):
    result = 0
    visited = [[0] * m for _ in range(n)]
    q = deque()
    q.append((x, y))
    visited[x][y] = 1

    while q:
        x, y = q.popleft()
        result = max(result, visited[x][y])
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] == 0 and arr[nx][ny] == 'L':
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))

    return result-1

answer = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 'L':
            answer = max(answer, bfs(i, j))

print(answer)










