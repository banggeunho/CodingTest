# 코딩테스트 대비 기초 문제 풀이 6일차
# Date : 2022. 01. 24.
# 구현(Implementation)에 관한 기초 문제 풀이


# 왕실의 나이트 (예제 4-2)
# 나이트는 8X8 형태의 좌표평면위에서 L자형태로만 이동가능하다.
# 1. 수평으로 두 칸 이동한 뒤에 수직을 한 칸 이동하기
# 2. 수직으로 두 칸 이동한 뒤에 수평으로 한 칸 이동하기
# 행 위치를 표현할 때는 1부터 8로 표현하여, 열 위치를 표현할 때는 A부터 H로 나타냄.


n = input()

# col은 알파벳으로 입력 받기 때문에, ASCII CODE로 변환하여 정수로 캐스팅한다.
row = int(n[1])
col = int(ord(n[0])) - int(ord('a')) + 1 

# 이동할 수 있는 모든 경우의 수
steps = [(2,1), (2,-1), (-2, 1), (-2, -1), (-1, 2), (1, 2), (1,-2), (-1, -2)]

count = 0
# 이동할 수 있는 모든 경우의 수 중에 이동했을때 8*8 안에 있는 것만 세어주면 된다.
for step in steps:
  next_row = row + step[0]
  next_col = col + step[1]

  # 정원의 사이즈에 만족할 때 카운트 적립
  if next_row >= 1 and next_row <= 8 and next_col >= 1 and next_col <= 8:
    count += 1

# 최종 결과 출력
print(count)


# 게임 개발 (예제 4-3)
# 구현 문제 / 시간제한 : 1초 / 메모리 제한 : 128MB
n, m = map(int, input().split())
x, y, direction = map(int, input().split())

d =  [[0]*m for _ in range(n)]
d[x][y] = 1

_map = list()
for i in range(n):
  _map.append(list(map(int, input().split())))


# 북:0, 동:1, 남:2, 서:3
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left():
  global direction
  direction -= 1
  if direction == -1:
    direction = 3


# 현재 위치, 방향을 기준으로 왼쪽부터 차례대로 갈 곳을 정함
# 캐릭터의 왼쪽 방향에 가보지 않은 칸이 존재하면, 왼쪽 방향으로 방향 회전 후, 왼쪽으로 한 칸 전진
# 왼쪽 방향에 가보지 않은 칸이 존재하지 않으면, 왼쪽 방향으로 회전 수행
# 만약 네 방향 모두 이미 가본 칸이거나 바다로 되어 있는 칸인 경우, 바라보는 방향을 유지한 채로
# 한 칸 뒤로 가고 1단께로 돌아간다. 단, 이때 뒤쪽 방향이 바다인 칸이라 뒤로 갈 수 없는 경우
# 움직임을 멈춘다.

count = 1
turn_time = 0
while True:
  turn_left()
  nx = x + dx[direction]
  ny = y + dy[direction]
  # 회전한 이후 정면에 가보지 않은 칸이 존재하면서, 육지일 경우 이동한다.
  if _map[nx][ny] == 0 and d[nx][ny] == 0:
    x = nx
    y = ny
    d[nx][ny] = 1
    count+=1
    turn_time = 0
    continue
  # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다이 ㄴ경우
  else:
    turn_time += 1
  
  # 이미 네 방향 모두 가본 경우
  if turn_time == 4:
    nx = x - dx[direction]
    ny = y - dy[direction]

  # 뒤쪽 방향이 바다인 경우
    if _map[nx][ny] == 1:
      break

  # 뒤쪽 방향이 바다가 아닌경우, x,y 를 이동한 좌표로 바꿔주고, turn_time을 0으로 초기화
    else:
      x = nx
      y = ny
    turn_time = 0
print(count)

