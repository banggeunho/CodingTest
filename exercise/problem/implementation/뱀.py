# 코딩테스트 대비 기초 문제 풀이 35일차
# Date : 2022. 02. 21.
# 구현 문제 풀이

#-------------------------****----------------------------------
# N의 범위가 500인 경우 : 시간 복잡도가 O(N^3)인 알고리즘을 설계
# N의 범위가 2,000인 경우 : 시간 복잡도가 O(N^2)인 알고리즘을 설계
# N의 범위가 100,000인 경우 : 시간 복잡도가 O(NlogN)인 알고리즘을 설계
# N의 범위가 10,000,000인 경우 : 시간 복잡도가 O(N)인 알고리즘을 설계
#-------------------------****----------------------------------

# 뱀
# 백준 3190

from collections import deque

n = int(input())
_map = [[0]*n for _ in range(n)]
k = int(input())
# 사과
for _ in range(k):
  a, b = map(int, input().split())
  _map[a-1][b-1] = 1

for i in range(n):
  for j in range(n):
    print(_map[i][j], end=' ')

  print()

# 시간, 명령어 저장할 dictionary 생성
time = {}
l = int(input())
for _ in range(l):
  a, b = input().split()
  time[int(a)] = b

t = 0
# 처음 방향은 오른쪽
dir = ['left', 'top', 'right', 'bottom']
dir_idx = 2

# 꼬리, 머리 위치
tail_x, tail_y = 0, 0
head_x, head_y = 0, 0

# 뱀을 큐로 표현
snake = deque()
# 맨첨 초깃값 넣어줌
snake.append((head_x, head_y))

while True:
  # 시간 추가
  t += 1

  # 방향 명령어 조회 -> 방향 설정
  if t-1 in time.keys():
    if time[t-1] == 'L':
      dir_idx -=1
      if dir_idx == -1:
        dir_idx = 3
    
    else:
      dir_idx +=1
      if dir_idx == 4:
        dir_idx = 0
    
  # 방향보고 대가리 움직임 설정 뱀의 머리가 먼저 움직임
  if dir[dir_idx] == 'right':
    head_y += 1

  elif dir[dir_idx] == 'bottom':
    head_x += 1

  elif dir[dir_idx] == 'top':
    head_x -= 1

  else:
    head_y -= 1

  # 뱀의 머리가 snake 큐 안에 있는 애들이랑 겹치면 ( 뱀이 자기자신과 만날때)
  if (head_x, head_y) in list(snake):
    break
  
  # 대가리가 범위를 벗어날경우 break
  if head_x >= n or head_y >= n or head_x < 0 or head_y < 0:
    break

  snake.append((head_x, head_y))

  # 사과가 없을 경우
  if _map[head_x][head_y] == 0:

      # 꼬리부분이 맨 앞이기 떄문에 pop left
      snake.popleft()
      if dir[dir_idx] == 'right':
        tail_y += 1

      elif dir[dir_idx] == 'bottom':
        tail_x += 1

      elif dir[dir_idx] == 'top':
        tail_x -= 1

      else:
        tail_y -= 1
  
  # 사과가 있으면 사과를 없애줌
  else:
    _map[head_x][head_y] = 0

print(t)