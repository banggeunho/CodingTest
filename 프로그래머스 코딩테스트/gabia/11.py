def solution(park, routes):
    answer = []
    op = {'E': (0, 1), 'W': (0, -1), 'N': (-1, 0), 'S': (1, 0)}
    W, H = len(park[0]), len(park)
    start = (0, 0)
    for i in range(H):
        for j in range(W):
            if 'S' == park[i][j]:
                start = (i, j)

    x, y = start
    for route in routes:
        direction, dist = route.split()
        for i in range(1, int(dist) + 1):
            x, y = x + op[direction][0], y + op[direction][1]
            if not (0 <= x < H and 0 <= y < W) or park[x][y] == 'X':
                x, y = x - op[direction][0] * i, y - op[direction][1] * i
                break

    return [x, y]


solution(["OSO","OOO","OXO","OOO"],	["E 2","S 3","W 1"])