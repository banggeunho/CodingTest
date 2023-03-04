import copy
from itertools import combinations
from collections import deque
n = int(input())
arr = []
teacher_idx = []
place_idx = []
for i in range(n):
    data = list(input().split())
    arr.append(data)
    for j in range(n):
        if data[j] == 'X':
            place_idx.append((i, j))
        elif data[j] == 'T':
            teacher_idx.append((i, j))


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# 장애물 설치하기
def install_wall(arr, case):
    for (i, j) in case:
        arr[i][j] = 'O'
    return arr

# 감시 가능한지 확인
def checkVisible(temp, x, y):
    q = deque()
    q.append((x, y, 0))
    q.append((x, y, 1))
    q.append((x, y, 2))
    q.append((x, y, 3))
    while q:
        cx, cy, direction = q.popleft()
        nx, ny = cx + dx[direction], cy + dy[direction]
        if 0 <= nx < n and 0 <= ny < n:
            if temp[nx][ny] == 'S':
                return True
            elif temp[nx][ny] == 'X':
                q.append((nx, ny, direction))

    return False

cases = list(combinations(place_idx, 3))

fail_count = 0
for case in cases:
    tmp_arr = copy.deepcopy(arr)
    tmp_arr = install_wall(tmp_arr, case)
    for (i, j) in teacher_idx:
        if checkVisible(tmp_arr, i, j):
            fail_count += 1
            break

if fail_count != len(cases):
    print('YES')
else:
    print('NO')