# 코딩테스트 대비 기초 문제 풀이 5일차
# Date : 2022. 01. 23.
# 구현(Implementation)에 관한 기초 문제 풀이


# 상하좌우 (예제 4-1)
# N*N 지도를 그리고, 여행가가 해당위치로 이동하게 명령 주입
# L, R, U, D를 통해 여행가가 움직이게 한다.

n = int(input())
cmd = list(input().split())

x, y = 1, 1

for command in cmd:
  # Move Left
  if command == 'L':
    if y-1 >= 1:
      y -= 1
  # Move Right
  elif command == 'R':
    if y+1 <= n:
      y += 1
  # Move UP
  elif command == 'U':
    if x-1 >= 1:
      x -= 1
  # Move Down
  else:
    if x+1 <= n:
      x += 1

print(x, y)

# 책 버젼

n = int(input())
x, y = 1, 1
plans = input().split()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:
  for i in range(len(move_types)):
    if plan == move_types[i]:
      nx = x + dx[i]
      ny = y + dy[i]
  
  if nx < 1 or ny < 1 or nx > n or ny > n:
    continue
  
  x, y = nx, ny

print(x, y)