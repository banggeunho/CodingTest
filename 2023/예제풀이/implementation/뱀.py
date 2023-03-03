# 오른쪽으로 회전
def turn_right(direction):
    return (direction + 1) % 4

# 왼쪽으로 회전
def turn_left(direction):
    return (direction - 1) % 4

# 각종 변수 설정
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
time = 0
direction = 2 # 오른 쪽 방향
n = int(input()) # 보드판 크기
k = int(input()) # 사과의 개수
head_x, head_y = 0, 0
body = [(0, 0)]

# 기본 맵 설정
arr = [[0] * n for _ in range(n)]

# 사과 위치 지정
for i in range(k):
    x, y = map(int, input().split())
    arr[x - 1][y - 1] = 1 # 사과는 1로 지정

l = int(input()) # 방향 변환 횟수
direction_change = []
for i in range(l):
    t, d = input().split()
    direction_change.append((int(t), d))

# simulation
while True:
    # print('------{}------'.format(time))
    # print('head', head_x, head_y)
    # print('direction', direction)
    # print('length', len(body))


    # 1. 뱀의 몸길이를 늘려 머리를 다음 칸에 위치
    head_x += dx[direction]
    head_y += dy[direction]

    # 자기 몸과 부딪힐 경우 종료
    if (head_x, head_y) in body:
        time += 1
        break

    # 몸 스택에 머리 추가
    body.append((head_x, head_y))

    # 벽에 부딕힐 경우 종료
    if not (0 <= head_x < n) or not (0 <= head_y < n):
        time += 1
        break

    # 2. 사과가 있는지 확인
    # 없다면 꼬리가 위치한 칸을 비워줌.
    if arr[head_x][head_y] != 1:
        body.pop(0)
    else:
        arr[head_x][head_y] = 0  # 사과를 없애 줍니다.

    # 3. 시간 추가
    time += 1
    # 방향 전환 확인
    for t, d in direction_change:
        if t == time:
            if d == 'L':
                direction = turn_left(direction)
            else:
                direction = turn_right(direction)
            break

print(time)


# 6
# 3
# 3 4
# 2 5
# 5 3
# 3
# 3 D
# 15 L
# 17 D

# 10
# 4
# 1 2
# 1 3
# 1 4
# 1 5
# 4
# 8 D
# 10 D
# 11 D
# 13 L