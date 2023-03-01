n, m = map(int, input().split())

visited = [[0] * m for i in range(n)] # 방문 기록

x, y, direction = map(int, input().split())
visited[x][y] = 1 # 방문처리

array = []
for i in range(n): # 지도 입력 받기
    array.append(list(map(int, input().split())))

# 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전하는 함수
def turn_left():
    global direction
    direction -= 1
    if direction == -1: # 순환되도록 설정
        direction = 3


count = 1 # 방문한 칸의 수
turn_time = 0 # 고개 돌리는 시간

while True:
    turn_left() # 왼쪽으로 회전
    nx = x + dx[direction]
    ny = y + dy[direction]

    # 회전한 이후 가보지 않은 칸이 존재 -> 전진
    if array[nx][ny] == 0 and visited[nx][ny] == 0: # 맵의 외곽은 항상 바다로 되어있어서 예외처리 안해줘도 된다...
        visited[nx][ny] = 1 # 방문처리
        x, y = nx, ny
        count += 1
        turn_time = 0
        continue

    else:
        turn_time += 1

    # 네 방향 모두 갈 수 없는 경우 (3번조건)
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]

        # 뒤로 갈 수 있다면 이동하기
        if array[nx][ny] == 0:
            x, y = nx, ny

        # 뒤에 바다면 끝
        else:
            break

        turn_time = 0

print(count)