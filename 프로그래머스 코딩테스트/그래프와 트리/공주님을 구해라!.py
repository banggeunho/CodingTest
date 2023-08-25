# https://www.acmicpc.net/problem/17836
from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs(hasWeapon, start, target):
    sx, sy = start
    q = deque([(sx, sy, 0)])
    visited[0][0] = True

    while q:
        x, y, time = q.popleft()

        if (x, y) == target and time <= T:
            return time

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if not hasWeapon:
                if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and data[nx][ny] != 1:
                    q.append((nx, ny, time + 1))
                    visited[nx][ny] = True
            else:
                if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                    q.append((nx, ny, time + 1))
                    visited[nx][ny] = True

    return float('inf')

N, M, T = map(int, input().split())
data = []
weapon_pos = ()
for i in range(N):
    data.append(list(map(int, input().split())))
    for j in range(M):
        if data[i][j] == 2:
            weapon_pos = (i, j)

visited = [[False] * M for _ in range(N)]
startToWeapon = bfs(False, (0, 0), weapon_pos)
visited = [[False] * M for _ in range(N)]
weaponToEnd = bfs(True, weapon_pos, (N-1, M-1))
visited = [[False] * M for _ in range(N)]
startToEnd = bfs(False, (0, 0), (N-1, M-1))

if (startToWeapon + weaponToEnd) <= T or startToEnd <= T:
    if startToWeapon + weaponToEnd <= startToEnd:
        print(startToWeapon + weaponToEnd)
    else:
        print(startToEnd)
else:
    print('Fail')