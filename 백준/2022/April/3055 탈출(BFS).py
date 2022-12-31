# 물과 고슴도치를 큐에 넣어서 각각 구분해서 움직이게끔 처리한다.
# 움직이는 개체가 2개 이상일 경우 이런 식으로 작성합시다.
from collections import deque
R, C = map(int, input().split())
arr = []
distance = [[0]*C for i in range(R)]
result = 0
q = deque()
for r in range(R):
    data = list(input())
    arr.append(data)
    for c in range(C):
        if arr[r][c] == '*':
           q.appendleft((r, c))
        if arr[r][c] == 'S':
            q.append((r, c))
        if arr[r][c] == 'D':
            Dx, Dy = r, c

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(Dx, Dy):
    while q:
        print(q)
        cx, cy  = q.popleft()
        if arr[Dx][Dy] == 'S': # 동굴 도착
            return distance[Dx][Dy]

        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < R and 0 <= ny < C:
                if (arr[nx][ny] == '.' or arr[nx][ny] == 'D') and arr[cx][cy] == 'S':
                    arr[nx][ny] = 'S'
                    distance[nx][ny] = distance[cx][cy] + 1
                    q.append((nx, ny))

                if (arr[nx][ny] == '.') and arr[cx][cy] == '*':
                    arr[nx][ny] = '*'
                    q.append((nx, ny))
    return 'KAKTUS'

print(bfs(Dx, Dy))