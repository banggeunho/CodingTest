n = int(input())

total = set()

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

arr = [[0] * 101 for _ in range(101)]

for _ in range(n):
    x, y, d, g = map(int, input().split())
    arr[x][y] = 1

    move = [d]

    for _ in range(g):
        temp = []
        # 기존 방향 배열을 거꾸로 뒤집고 1씩 더한 것.
        for i in range(len(move)):
            temp.append((move[-i - 1] + 1) % 4)

        move.extend(temp)

    # 드래곤 커브에 해당하는 좌표의 값을 1로 변경
    for i in move:
        nx = x + dx[i]
        ny = y + dy[i]
        arr[nx][ny] = 1
        x, y, = nx, ny

result = 0
for i in range(100):
    for j in range(100):
        if arr[i][j] and arr[i+1][j] and arr[i][j+1] and arr[i+1][j+1]:
            result += 1

print(result)