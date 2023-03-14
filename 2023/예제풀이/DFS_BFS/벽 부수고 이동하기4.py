from collections import deque

# 방향 설정
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# 너비 우선 탐색
def bfs(start):
    x, y = start
    q = deque()
    q.append((x, y))
    visited[x][y] = True

    count = 0 # 결과값 리턴
    while q:
        cx, cy = q.popleft()
        count += 1
        # 그룹을 나타내는 list에 그룹 선정
        zeros[cx][cy] = group

        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 0:
                if not visited[nx][ny]:
                    q.append((nx, ny))
                    visited[nx][ny] = True

    return count

# 이동할 수 있는 위치 세기
def move_count(x, y):
    data = set() # 인접 위치에 있는 그룹들을 저장하기 위한 set
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and zeros[nx][ny]:
            data.add(zeros[nx][ny])

    cnt = 1 # 자기 자신 먼저 카운트

    for g in data: # 그룹별 이동할 수 있는 위치 저장
        cnt += info[g]

    return cnt % 10

# input = sys.stdin.readline
n, m = map(int, input().split())

arr = []
wall_idx = []

for i in range(n):
    data = list(map(int, input()))
    arr.append(data)


zeros = [[0] * m for _ in range(n)] # 그룹을 나타내기 위한 list
visited = [[False] * m for _ in range(n)] # 방문 list

# 그룹 지정(0인 수가 몇개 있는지 확인) bfs 사용
group = 1
info = {}
for i in range(n):
    for j in range(m):
        if not arr[i][j] and not visited[i][j]:
            info[group] = bfs((i, j))
            group += 1


# 벽인 공간을 찾아, 몇 개의 공간이 있는지 확인
for i in range(n):
    for j in range(m):
        if arr[i][j]:
            arr[i][j] = move_count(i, j)

# 결과 출력
for i in range(n):
    for j in range(m):
        print(arr[i][j], end='')
    print()