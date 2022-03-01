# 코딩테스트 대비 기초 문제 풀이 40일차
# Date : 2022. 03. 02.
# 구현 문제 풀이
# https://www.acmicpc.net/problem/14502
#-------------------------****----------------------------------
# N의 범위가 500인 경우 : 시간 복잡도가 O(N^3)인 알고리즘을 설계
# N의 범위가 2,000인 경우 : 시간 복잡도가 O(N^2)인 알고리즘을 설계
# N의 범위가 100,000인 경우 : 시간 복잡도가 O(NlogN)인 알고리즘을 설계
# N의 범위가 10,000,000인 경우 : 시간 복잡도가 O(N)인 알고리즘을 설계
#-------------------------****----------------------------------
#4615. 재미있는 오셀로 게임
for tc in range(1, int(input())+1):
  N, M = map(int, input().split())
  grid = [[0]*(N+1) for _ in range(N+1)]
  grid[N//2][N//2] = grid[N//2+1][N//2+1] = 2
  grid[N//2][N//2+1] = grid[N//2+1][N//2] = 1

   # 2가 백, 1이 흑
  dx = [-1, -1, -1, 0, 0, 1, 1, 1]
  dy = [-1, 0, 1, -1, 1, -1 ,0, 1]
  for _ in range(M):
    x, y, color = map(int, input().split())
    grid[x][y] = color
    
    for k in range(8):
      nx = x+dx[k]
      ny = y+dy[k]
      cnt = 0
 
      while N >= nx > 0 and N >= ny > 0:
        if grid[nx][ny] != color and grid[nx][ny] != 0:
          cnt += 1
          nx = nx + dx[k]
          ny = ny + dy[k]
        elif grid[nx][ny] == color:
          for c in range(1, cnt+1):
            grid[x+(dx[k]*c)][y+(dy[k]*c)] = color
          break
        else:
          break

  black = white = 0
  for j in grid:
      black += j.count(1)
      white += j.count(2)
        
  print(f'#{tc} {black} {white}')
  # print(''.join(str))
  
    

  
  