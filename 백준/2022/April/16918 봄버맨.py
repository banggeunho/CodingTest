# 구현 + 그래프(bfs) 문제
from collections import deque
r, c, n = map(int, input().split())
time = 1
visited = [[0]*c for _ in range(r)]
arr = []
for i in range(r):
    arr.append(list(input()))
    for j in range(c):
        if arr[i][j] == 'O':
            visited[i][j] = 1 # 폭탄설치 - 초기시간 1

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# 전체 그래프 출력
def printResult():
    for i in range(r):
        for j in range(c):
            print(arr[i][j], end='')
        print()

# 폭탄 설치
def installation():
    global time
    time += 1 # 시간 1 증가
    for i in range(r):
        for j in range(c):
            if arr[i][j] == '.': # 폭탄이 아닐 경우
                arr[i][j] = 'O' # 설치 - 초기시간 1
                visited[i][j] = 1
            else: # 폭탄일 경우 -> 시간 증가
                visited[i][j] += 1

# 폭탄 터트리기
def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = 0 # 폭탄 터트리기
    arr[x][y] = '.'

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < r and 0 <= ny < c: # 시간이 다 된 폭탄인 경우(폭탄 주변 다 터드려야함)
                if arr[nx][ny] == 'O' and visited[nx][ny] == 2: # 시간이 덜 된 것은 연쇄반응 X
                    q.append((nx, ny)) 
                visited[nx][ny] = 0
                arr[nx][ny] = '.'

# n %= 4
# 짝수인 경우는 무조건 폭탄이 다 설치된 모습이 출력
if n % 2 == 0:
    for i in range(r):
        for j in range(c):
            print('O', end='')
        print()

# 아닌 경우 정상적으로 진행
else:
    while time != n:
        installation() # 설치시 TIME 1 증가
        if time == n: # TIME 비교
            break

        time += 1 # 폭탄 터트리기 TIME 1 증가
        for i in range(r):
            for j in range(c):
                if arr[i][j] == 'O' and visited[i][j] == 2:
                    bfs(i, j)

        if time == n: # TIME 비교
            break

    printResult()
