
# 코딩테스트 대비 기초 문제 풀이 
# Date : 2022. 03. 26.
# 삼성전자 기출 문제
#-------------------------****----------------------------------
# N의 범위가 500인 경우 : 시간 복잡도가 O(N^3)인 알고리즘을 설계
# N의 범위가 2,000인 경우 : 시간 복잡도가 O(N^2)인 알고리즘을 설계
# N의 범위가 100,000인 경우 : 시간 복잡도가 O(NlogN)인 알고리즘을 설계
# N의 범위가 10,000,000인 경우 : 시간 복잡도가 O(N)인 알고리즘을 설계
#-------------------------****------------------------------------

arr = [[]*4 for _ in range(4)]
loc = []
# fish_info = []*16
for i in range(4):
  data = list(map(int, input().split()))
  j = 0
  for k in range(0, 8, 2):
    arr[i].append((data[k], data[k+1]))
    loc.append((data[k], i, j))
    j += 1

print(arr)
loc.sort()

sx, sy = 0, 0 # 상어 위치
arr[0][0] = 0
dx = [0, -1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 0, -1, -1, -1, 0, 1, 1, 1]


for num, x, y in loc:
  if arr[x][y] != 0: # 물고기가 있는 경우
    _, dir = arr[x][y]
    nx = x + dx[dir]
    ny = y + dy[dir]
    exchange = False

    if 0 <= nx < 4 and 0 <= ny < 4: # 범위
      if (nx != sx and ny != sy) and arr[nx][ny][0] > 0: # 상어의 위치x, 물고기가 있는 경우
        num2, _ = arr[nx][ny]
        arr[x][y], arr[nx][ny] = arr[nx][ny], arr[x][y] # 지도 위치 변경
        loc.remove((num, x, y))
        loc.remove((num2, nx, ny))
        loc.insert(num-1, (num, nx, ny))
        loc.insert(num2-1, (num2, x, y))
        print(f'exchange {num} <-> {num2}')
        exchange = True

    if not exchange: # 자리 교환이 안됐을 경우
      for i in range(1, 7):
        n_dir = dir + i
        
        if n_dir > 7:
          n_dir %= 8
          
        nx = x + dx[n_dir]
        ny = y + dy[n_dir]

        if 0 <= nx < 4 and 0 <= ny < 4: # 범위
          if (nx != sx and ny != sy) and arr[nx][ny][0] > 0: # 상어의 위치x, 물고기가 있는 경우 
            num2, _ = arr[nx][ny]
            arr[x][y], arr[nx][ny] = arr[nx][ny], arr[x][y]
            loc.remove((num, x, y))
            loc.remove((num2, nx, ny))
            loc.insert(num-1, (num, nx, ny))
            loc.insert(num2-1, (num2, x, y))
            exchange = True
            print(f'exchange {num} <-> {num2}')

        if exchange:
          break

  print(loc)

print(arr)
            