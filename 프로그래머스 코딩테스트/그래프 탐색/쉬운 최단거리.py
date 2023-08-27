from collections import deque

# 지도의 크기 입력 받기
n, m = map(int, input().split())

# 지도 정보 입력 받기
map_data = []
for _ in range(n):
    row = list(map(int, input().split()))
    map_data.append(row)

# 목표 지점 찾기
target_x, target_y = -1, -1
for i in range(n):
    for j in range(m):
        if map_data[i][j] == 2:
            target_x, target_y = i, j
            break

# 방향 설정 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS 탐색
def bfs():
    distance = [[-1] * m for _ in range(n)]
    distance[target_x][target_y] = 0
    queue = deque([(target_x, target_y)])

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and distance[nx][ny] == -1:
                if map_data[nx][ny] == 1:
                    distance[nx][ny] = distance[x][y] + 1
                    queue.append((nx, ny))
                elif map_data[nx][ny] == 0:
                    distance[nx][ny] = 0

    return distance

# BFS 실행 및 결과 출력
result = bfs()
for i in range(n):
    for j in range(m):
        if map_data[i][j] == 0:
            print(0, end=" ")
        else:
            print(result[i][j], end=" ")
    print()
