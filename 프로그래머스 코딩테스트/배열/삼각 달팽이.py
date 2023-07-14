# 처음 버전

dx = [1, 0, -1]
dy = [0, 1, -1]


def getMaxNum(n):
    return sum([i for i in range(1, n + 1)])


def solution(n):
    max_num = getMaxNum(n)
    matrix = [[0] * n for _ in range(n)]
    answer = []

    x, y = 0, 0
    direction = 0
    num_count = 1
    matrix[x][y] = 1

    while True:
        nx, ny = x + dx[direction], y + dy[direction]

        # 방향 전환
        if not (0 <= nx < n and 0 <= ny < n) or matrix[nx][ny] != 0:
            if num_count >= max_num:
                break

            direction = (direction + 1) % 3
            continue

        num_count += 1

        x, y = nx, ny
        matrix[nx][ny] = num_count

        for row in matrix:
            print(row)
        print()

    for i in range(n):
        for j in range(n):
            if matrix[i][j] != 0:
                answer.append(matrix[i][j])

    return answer


print(solution(6))


## 개선 버전

def solution(n):
    res = [[0] * i for i in range(1, n + 1)]
    y, x = -1, 0
    num = 1

    for i in range(n):
        for j in range(i, n):
            angle = i % 3

            if angle == 0:
                y += 1
            elif angle == 1:
                x += 1
            elif angle == 2:
                y -= 1
                x -= 1

            res[y][x] = num
            num += 1

    return [i for j in res for i in j]