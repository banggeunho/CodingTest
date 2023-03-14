def move_dice(cmd, dice_v, dice_h):
    if cmd == 1: # 동
        dice_h[0], dice_h[1], dice_h[2], dice_v[3] = dice_v[3], dice_h[0], dice_h[1], dice_h[2]
        dice_v[1] = dice_h[1]

    elif cmd == 2: # 서
        dice_h[0], dice_h[1], dice_h[2], dice_v[3] = dice_h[1], dice_h[2], dice_v[3], dice_h[0]
        dice_v[1] = dice_h[1]

    elif cmd == 3: # 북
        dice_v[0], dice_v[1], dice_v[2], dice_v[3] = dice_v[1], dice_v[2], dice_v[3], dice_v[0]
        dice_h[1] = dice_v[1]

    else: # 남
        dice_v[0], dice_v[1], dice_v[2], dice_v[3] = dice_v[3], dice_v[0], dice_v[1], dice_v[2]
        dice_h[1] = dice_v[1]



# 입력
n, m, x, y, k = map(int, input().split())

arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

commands = list(map(int, input().split()))

# 주사위 전개도
dice_v = [0, 0, 0, 0]
dice_h = [0, 0, 0]

# 이동뱡향 인덱스 0자리는 문제 조건과 맞추기 위해 설정.
dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]


for cmd in commands:
    x, y = x + dx[cmd], y + dy[cmd]
    if 0 <= x < n and 0 <= y < m: # 주사위를 움직였을 때, 범위 안에 있는 경우
        move_dice(cmd, dice_v, dice_h)
        if arr[x][y] == 0: # 지도 바닥 칸이 0일 경우, 주사위 바닥면의 수를 복사
            arr[x][y] = dice_v[3]
        else: # 지도 바닥 칸이 0이 아니면, 주사위 바닥면에 복사 후 자신은 0으로 초기화
            dice_v[3] = arr[x][y]
            arr[x][y] = 0
        print(dice_h[1]) # 주사위 윗면
    else:
        x, y = x - dx[cmd], y - dy[cmd] # 범위를 초과하면 연산 초기화
        continue

