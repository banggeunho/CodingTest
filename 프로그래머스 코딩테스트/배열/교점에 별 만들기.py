# https://school.programmers.co.kr/learn/courses/30/lessons/87377?language=python3
def solution(line):
    meet = []
    n = len(line)
    x_min = y_min = float('inf')
    x_max = y_max = -float('inf')

    for i in range(n):
        a, b, e = line[i]
        for j in range(i + 1, n):
            c, d, f = line[j]

            if a * d != b * c:
                x = ((b * f) - (e * d)) / ((a * d) - (b * c))
                y = ((e * c) - (a * f)) / ((a * d) - (b * c))

                if x.is_integer() and y.is_integer():
                    x, y = int(x), int(y)
                    meet.append((x, y))
                    x_max, y_max = max(x_max, x), max(y_max, y)
                    x_min, y_min = min(x_min, x), min(y_min, y)

    width = abs(x_max - x_min) + 1
    height = abs(y_max - y_min) + 1
    answer = [['.'] * width for _ in range(height)]
    meet = sorted(meet, key=lambda i: -i[1])

    for x, y in meet:
        ny = y_max - y
        nx = x - x_min
        answer[ny][nx] = '*'

    return list(map(''.join, answer))

print(solution([[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]))
