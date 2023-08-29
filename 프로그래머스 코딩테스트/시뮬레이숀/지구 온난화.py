# https://www.acmicpc.net/problem/5212

r, c = map(int, input().split())
arr = []
ground_positions = []

for i in range(r):
    temp = list(input())
    arr.append(temp)
    for j in range(c):
        if temp[j] == 'X':
            ground_positions.append((i, j))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
def is_after_wrapping(x, y):
    count = 0
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if not (0 <= nx < r and 0 <= ny < c):
            count += 1
            continue
        if arr[nx][ny] == '.':
            count += 1
        else:
            continue

    return count >= 3

r_range = (0, r)
c_range = (0, c)

def remove_sea():
    global r_range, c_range, r, c
    new_r = new_c = tuple()

    for j in range(c_range[0], c_range[1]):
        if arr[r_range[0]][j] != '.':
            break
    else:
        new_r = (r_range[0] + 1, r_range[1])

    for j in range(c_range[0], c_range[1]):
        if arr[r_range[1] - 1][j] != '.':
            break
    else:
        new_r = (r_range[0], r_range[1] - 1)

    for j in range(r_range[0], r_range[1]):
        if arr[j][c_range[0]] != '.':
            break
    else:
        new_c = (c_range[0] + 1, c_range[1])

    for j in range(r_range[0], r_range[1]):
        if arr[j][c_range[1] - 1] != '.':
            break
    else:
        new_c = (c_range[0], c_range[1] - 1)

    return new_r, new_c


for x, y in ground_positions:
    if is_after_wrapping(x, y):
        arr[x][y] = '#' # 별도의 문양으로 바꿔놓자

for i in range(r):
    for j in range(c):
        if arr[i][j] == '#':
            arr[i][j] = '.'

# 테두리 제거하기
while True:
    # print(r_range, c_range)
    new_r, new_c = remove_sea()
    if not new_r and not new_c:
        break

    if new_r:
        r_range = new_r
        r = new_r[1]
    if new_c:
        c_range = new_c
        c = new_c[1]

for i in range(r_range[0], r_range[1]):
    for j in range(c_range[0], c_range[1]):
        print(arr[i][j], end='')
    print()







