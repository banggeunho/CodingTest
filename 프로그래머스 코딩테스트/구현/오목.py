arr = [list(map(int, input().split())) for _ in range(19)]

def check_win(pos, color, dx, dy):
    x, y = pos
    for i in range(1, 5):
        nx, ny = x + dx * i, y + dy * i
        if not (0 <= nx < 19 and 0 <= ny < 19) or color != arr[nx][ny]:
            return False
    if 0 <= x - dx < 19 and 0 <= y - dy < 19 and color == arr[x - dx][y - dy]:
        return False
    if 0 <= x + dx * 5 < 19 and 0 <= y + dy * 5 < 19 and color == arr[x + dx * 5][y + dy * 5]:
        return False
    return True

solve = False
for i in range(19):
    for j in range(19):
        if arr[i][j] != 0:
            directions = [(0, 1), (1, 0), (1, 1), (-1, 1)]
            for dx, dy in directions:
                if check_win((i, j), arr[i][j], dx, dy):
                    print(arr[i][j])
                    print(i + 1, j + 1)
                    solve = True
                    break

        if solve:
            break

    if solve:
        break

if not solve:
    print(0)
