# 18428 감시피하기

import itertools

arr = []
x_pos = []
solve = True
n = int(input())
for i in range(n):
  arr.append(list(input().split()))
  for j in range(n):
    if arr[i][j] == 'X':
      x_pos.append((i, j))

candidates = itertools.combinations(x_pos, 3)

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def dfs(x, y, arr):
  global dx, dy, n
  # print(x, y)
  
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]

    if nx < 0 or nx >=n or ny < 0 or ny >= n:
      continue
      
    # print('사방향 검사', nx, ny)
    if arr[nx][ny] == 'S':
      # print('학생 찾음')
      return False

    if arr[nx][ny] == 'O':
      # print('장애물')
      continue
    
    if arr[nx][ny] == 'X':
      while True:
        nx += dx[i]
        ny += dy[i]

        if nx < 0 or nx >=n or ny < 0 or ny >= n:
          break
          
        # print('진입',nx,ny)
        if arr[nx][ny] == 'O':
          # print('장애물')
          break

        if arr[nx][ny] == 'S':
          # print('학생 찾음')
          return False
          
  return True

    
for candidate in candidates:   
  solve = True
  for x, y in candidate:
    arr[x][y] = 'O'

  # for i in range(n):
  #   for j in range(n):
  #     print(arr[i][j], end=' ')
  #   print()
    
  for i in range(n):
    for j in range(n):
      if arr[i][j] == 'T' and solve:
        solve = dfs(i, j, arr)


  if solve:
    print('YES')
    break

  for x, y in candidate:
    arr[x][y] = 'X'
    
if not solve:
  print('NO')