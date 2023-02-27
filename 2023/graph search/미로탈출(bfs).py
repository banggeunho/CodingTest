from collections import deque

n, m = map(int, input().split())

arr = [] # 미로 정보 입력받기
for i in range(n):
    arr.append(list(map(int, input())))

visited = [[0] * m for i in range(n)] # 방문 그래프 생성

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(graph, start, visited):
    x, y = start
    q = deque()
    q.append((x, y, 1)) # 마지막 거리 값 추가
    visited[x][y] = 1 # 방문처리

    while q:
        cx, cy, dist = q.popleft()
        print(cx, cy, dist)
        if cx == n-1 and cy == m-1: # 목적지 도착 시 종료
            return dist
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1 and visited[nx][ny] == 0:
                q.append((nx, ny, dist+1)) # 거리 +1 추가
                visited[nx][ny] = 1


print(bfs(arr, (0, 0), visited))
