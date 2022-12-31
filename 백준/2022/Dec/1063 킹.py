# 입력 받기
col = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
k_loc, s_loc, n = input().split()
k_x, k_y = ord(k_loc[0]) - ord('A'), int(k_loc[1]) - 1
s_x, s_y = ord(s_loc[0]) - ord('A'), int(s_loc[1]) - 1

def movePlayer(dx, dy):
  global k_x, k_y, s_x, s_y
  k_nx, k_ny = k_x + dx, k_y + dy
  
  # 지도에서 나갈 경우
  if 0 <= k_nx < 8 and 0 <= k_ny < 8:
    # k_x, k_y = k_nx, k_ny
    # 돌과 같은 곳으로 이동할 경우
    if s_x == k_nx and s_y == k_ny:
      # 돌을 밀어낸다 같은 방향으로
      s_nx, s_ny = s_x + dx, s_y + dy
      # 돌이 지도 밖으로 나가지 않을 경우
      if 0 <= s_nx < 8 and 0 <= s_ny < 8:
        k_x, k_y = k_nx, k_ny
        s_x, s_y = s_nx, s_ny
    # 돌이 있는 곳으로 이동 X
    else:
      k_x, k_y = k_nx, k_ny
      
  # print('king ; ', k_x, k_y)
  # print('dol ; ', s_x, s_y)

for i in range(int(n)):
  cmd = input()

  if cmd == 'R':
    movePlayer(1, 0)

  if cmd == 'L':
    movePlayer(-1, 0)

  if cmd == 'B':
    movePlayer(0, -1)

  if cmd == 'T':
    movePlayer(0, 1)

  if cmd == 'RT':
    movePlayer(1, 1)

  if cmd == 'LT':
    movePlayer(-1, 1)

  if cmd == 'RB':
    movePlayer(1, -1)

  if cmd == 'LB':
    movePlayer(-1, -1)

# 결과 출력
k_res = f'{col[k_x]}{k_y+1}'
s_res = f'{col[s_x]}{s_y+1}'
print(k_res)
print(s_res)