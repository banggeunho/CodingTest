# DFS 문제
# <풀이 키포인트>
# N의 숫자가 적으므로 물고기의 이동을 매번 수행시켜줘도 무방함
# DFS를 이용할땐 재귀적으로 호출될때마다 각자 독립된 array를 사용하기 위해 deepcopy를 이용한다.
# 8개의 방향이 움직일떄 나머지 연산을 이용한다.
# 문제에서 요구한 순서대로 코드를 작성하면 된다.

import copy
arr = [[] for _ in range(4)]
# fish = [[] for _ in range(16)]
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]
answer = 0

for i in range(4):
    data = list(map(int, input().split()))
    for k in range(0, 8, 2):
        arr[i].append([data[k], data[k+1]-1]) # 물고기 위치, 방향 저장
        # fish[data[k]] = [i, k//2]  # 물고기 위치 저장


# 특정 물고기 위치 찾는 함수(없으면 None 반환)
def find_fish(arr, index):
    for i in range(4):
        for j in range(4):
            if arr[i][j][0] == index:
                return (i, j)
    return None

def move_fish(array, now_x, now_y):
    for i in range(1, 17):
        position = find_fish(array, i)
        if position is None:
            continue
        x, y = position
        dir = array[x][y][1] # 방향 가쟈오기
        for _ in range(8):
            nx, ny = x + dx[dir], y + dy[dir]
            if 0 <= nx < 4 and 0 <= ny < 4:
                if not (nx == now_x and ny == now_y): # 공간의 범위 안에 있고, 상어가 없을 경우
                    array[x][y][0], array[nx][ny][0] = array[nx][ny][0], array[x][y][0]
                    array[x][y][1], array[nx][ny][1] = array[nx][ny][1], dir
                    break
            dir = (dir + 1) % 8

def food(array, x, y):
    positions = []
    direction = array[x][y][1]
    for i in range(1, 4):
        nx, ny = x + dx[direction], y + dy[direction]
        if 0 <= nx < 4 and 0 <= ny < 4 and 1 <= array[nx][ny][0] <= 16: # 범위 안에 있으며, 물고기인 것]
            positions.append((nx, ny))
        x, y = nx, ny
    return positions

def dfs(arr, x, y, total):
    global answer
    arr = copy.deepcopy(arr)
    number = arr[x][y][0]
    arr[x][y][0] = -1 # 먹었음
    move_fish(arr, x, y)
    result = food(arr, x, y)
    answer = max(answer, total+number)
    for next_x, next_y in result:
        dfs(arr, next_x, next_y, total + number)

dfs(arr, 0, 0, 0)
print(answer)