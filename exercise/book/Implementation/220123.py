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

# 시각 (예제 4-2)
# 입력 : N
# 00시 00분 00초부터 N시 59분 59초까지 중 3이 하나라도 포함되는     
# 모든경우의 수를 구한다.

n = int(input())
count = 0
# 0시 부터 N시
for k in range(n+1):
  # 시간에 3이 포함되어 있으면,  60분 * 60초 = 3600 추가
  if k % 10 == 3 or int(k/10) == 3:
      count += 3600
  # 시간에 3이 포함되어 있지 않으면, 분을 본다.
  else:
    for i in range(60):
      # 분에 3이 포함되어 있으면, 60초 = 60 추가
      if i % 10 == 3 or int(i/10) == 3:
        count += 60
      # 분에 3이 포함되어 있지 않으면
      else:
        for j in range(60):
          # 0부터 59까지 보면서 3이 있으면 1 추가
          if j % 10 == 3 or int(j/10) == 3:
            count += 1

print( count )

# 책 버전
# 시분초를 '030403' 스트링으로 바꿔서 '3'이 포함되어 있으면 카운트 증가
h = int(input())

count = 0
for i in range(h+1):
  for j in range(60):
    for k in range(60):
      # 매 시각 안에 '3' 포함되어 있다면 카운트 증가
      if '3' in str(i) + str(j) + str(k):
        count += 1

print(count)