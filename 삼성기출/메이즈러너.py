# https://www.codetree.ai/training-field/frequent-problems/problems/maze-runner/description?page=1&pageSize=20
from copy import deepcopy

N, M, K = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]
person_pos = []
for _ in range(M):
    x, y = map(int, input().split())
    person_pos.append((x - 1, y - 1))

exit_pos = tuple(map(int, input().split()))
exit_pos = (exit_pos[0] - 1, exit_pos[1] - 1)
moved_pos = []
answer = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def cal_min_distance(current, exit):
    x, y = current
    x1, y1 = exit
    return abs(x - x1) + abs(y - y1)


def rotate_90_degrees_clockwise(matrix, top_left_pos, square_size):
    global exit_pos

    if not matrix:
        return matrix

    # square_len = abs(top_right_pos[1] - top_left_pos[1]) + 1
    # print("정사각형 크기", square_size)

    # 새로운 2차원 리스트 생성
    rotated_matrix = [[0] * N for _ in range(N)]
    # print(top_left_pos)
    sx, sy = top_left_pos[0], top_left_pos[1]
    rotated_person = []
    rotated_exit = tuple()

    for i in range(sx, sx + square_size):
        for j in range(sy, sy + square_size):
            ox, oy = i - sx, j - sy
            rx, ry = oy, square_size - 1 - ox
            if matrix[i][j] > 0:
                rotated_matrix[rx + sx][ry + sy] = matrix[i][j] - 1
            else:
                rotated_matrix[rx + sx][ry + sy] = matrix[i][j]
                if exit_pos == (i, j) and not rotated_exit:
                    # print('출구 이동 ', i ,j , ' ->', rx + sx, ry +sy)
                    rotated_exit = (rx + sx, ry + sy)
            # print(i, j, '->', rx + sx, ry + sy)

    for i in range(len(moved_pos)):
        tx, ty = moved_pos[i]
        if sx <= tx < sx + square_size and sy <= ty < sy + square_size:
            ox, oy = tx - sx, ty - sy
            rx, ry = oy, square_size - 1 - ox
            moved_pos[i] = ((rx + sx, ry + sy))

    exit_pos = rotated_exit

    return rotated_matrix


time = 0
while time < K and person_pos:
    # print(time + 1, '===========')
    time += 1
    moved_pos.clear()

    for idx, (x, y) in enumerate(person_pos):
        temp_pos = []
        current_dis = cal_min_distance((x, y), exit_pos)
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            next_dis = cal_min_distance((nx, ny), exit_pos)
            if 0 <= nx < N and 0 <= ny < N and data[nx][ny] == 0 and current_dis > next_dis:
                temp_pos.append((i, nx, ny))
                break

        if temp_pos:
            temp_pos.sort()
            if (temp_pos[0][1], temp_pos[0][2]) == exit_pos:
                answer += 1
            else:
                temp_pos[0]
                moved_pos.append((temp_pos[0][1], temp_pos[0][2]))
                answer += 1
        else:
            moved_pos.append((x, y))

    if len(moved_pos) == 0:
        break

    # print('이동했음 ', moved_pos, exit_pos)

    has_person = False
    top_left_pos, top_right_pos = (), ()
    bottom_left_pos, bottom_right_pos = (), ()
    square_size = 0
    for i in range(1, N - 1):
        for j in range(N - i):
            for k in range(N - i):
                # print(i, j, k)
                e_x, e_y = exit_pos
                # 출구가 정사각형 안에 있는지
                if j <= e_x <= j + i and k <= e_y <= k + i:
                    # print('출구 존재')
                    for pos in moved_pos:
                        p_x, p_y = pos
                        if j <= p_x <= j + i and k <= p_y <= k + i:
                            # print('사람 존재:', p_x, p_y, j, k, '크기', i)
                            has_person = True
                            top_left_pos, top_right_pos = (j, k), (j, k + i)
                            bottom_left_pos, bottom_right_pos = (j + i, k), (j + i, k + i)
                            square_size = i + 1
                            break

                if has_person:
                    break

            if has_person:
                break

        if has_person:
            break

    # print('정사각형' ,top_left_pos, top_right_pos, bottom_left_pos, bottom_right_pos)
    rotated_matrix = rotate_90_degrees_clockwise(data, top_left_pos, square_size)

    for i in range(top_left_pos[0], bottom_left_pos[0] + 1):
        for j in range(top_left_pos[1], top_right_pos[1] + 1):
            data[i][j] = rotated_matrix[i][j]

    # print(rotated_matrix)
    # print(data, rotated_pos)
    person_pos = deepcopy(moved_pos)

    # for i in range(N):
    #     for j in range(N):
    #         if (i, j) == exit_pos:
    #             print("e", end = ' ')
    #         else: print(data[i][j], end = ' ')
    #     print()

    # print(person_pos, exit_pos, answer)

print(answer)
print(exit_pos[0] + 1, exit_pos[1] + 1)



# 5 8 3
# 0 3 3 0 7
# 3 0 4 2 0
# 0 2 0 6 6
# 0 8 6 7 4
# 8 0 8 5 0
# 1 1
# 5 2
# 1 1
# 2 5
# 1 1
# 2 2
# 2 5
# 5 2
# 5 5
