# N X M 크기와 4개의 버튼
# 각각의 칸은 비어있거나, 벽이다.
# 버튼은 왼쪽, 오른쪽, 위, 아래와 같이 4가지가 있음.
# 버튼을 누르면 두 동전이 버튼에 쓰여 있는 방향으로 이동
# - 동전이 이동하려는 방향의 칸이 벽이면, 동전이 이동 X
# - 동전이 이동하려는 방향에 칸이 없으면 동전은 보드 바깥으로 떨어진다.
# - 그 외의 경우에는 이동하려는 방향으로 한 칸 이동한다. 이동하려는 칸에 동전이 있는 경우에도 똑같이 이동
# 두 동전 중 하나만 보드에서 떨어뜨리기 위해 버튼을 최소 몇 번 눌러야하는지 구하는 프로그램을 작성하시오.
#    # - 벽, . - 빈 칸, o - 동전


# 움직이는 개체가 2개인 bfs 문제
from collections import deque
n, m = map(int, input().split())
arr = []
coin_idx = []
solve = False

for i in range(n):
    data = list(input())
    arr.append(data)
    for j in range(m):
        if arr[i][j] == 'o':
            coin_idx.append((i, j))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

q = deque()
q.append((coin_idx[0][0], coin_idx[0][1], coin_idx[1][0], coin_idx[1][1], 0))

while q:
    c1_x, c1_y, c2_x, c2_y, cost = q.popleft()

    if cost >= 10:
        print(-1)
        break

    for i in range(4):
        c1_nx, c1_ny = c1_x + dx[i], c1_y + dy[i]
        c2_nx, c2_ny = c2_x + dx[i], c2_y + dy[i]
        # 범위 안에 있을 경우
        if (0 <= c1_nx < n and 0 <= c1_ny < m) and (0 <= c2_nx < n and 0 <= c2_ny < m):
            if arr[c1_nx][c1_ny] == '#':
                c1_nx, c1_ny = c1_x, c1_y

            if arr[c2_nx][c2_ny] == '#':
                c2_nx, c2_ny = c2_x, c2_y

            q.append((c1_nx, c1_ny, c2_nx, c2_ny, cost+1))

        # 동전 2가 떨어졌을 경우
        elif 0 <= c1_nx < n and 0 <= c1_ny < m:
            print(cost + 1)
            solve = True
            break
        # 동전 1이 떨어졌을 경우
        elif 0 <= c2_nx < n and 0 <= c2_ny < m:
            print(cost + 1)
            solve = True
            break

        # 둘다 떨어졌을 경우
        else:
            continue

    if solve:
        break