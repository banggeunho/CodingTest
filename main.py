# 코딩테스트 대비 기초 문제 풀이 
# Date : 2022. 03. 26.
# 삼성전자 기출 문제
#-------------------------****----------------------------------
# N의 범위가 500인 경우 : 시간 복잡도가 O(N^3)인 알고리즘을 설계
# N의 범위가 2,000인 경우 : 시간 복잡도가 O(N^2)인 알고리즘을 설계
# N의 범위가 100,000인 경우 : 시간 복잡도가 O(NlogN)인 알고리즘을 설계
# N의 범위가 10,000,000인 경우 : 시간 복잡도가 O(N)인 알고리즘을 설계
#-------------------------****------------------------------------

# 상어 초등학교 (구현 기출 문제)
# N의 갯수가 최대 20개이므로 N^4이어도 최대 16000개의 경우의 수
# 순차 탐색으로 주어진 조건만 잘 맞춰서 작성하면 무리가 없는 문제

# 각 입력을 받을때마다 순차적으로 전체 map을 확인하면서
# 조건에 맞는 위치에 학생의 번호를 넣어줘야한다.
# 각 조건의 맞는 위치를 찾아 하나의 list(조건이 담긴)로 만들어
# 최종적으로 위치들의 후보들을 갖고 정렬을 수행해 적절한 위치를 뽑아내어 학생으로 업데이트 해준다.

# 자리 배치가 완성되면 처음부터 map을 살펴보면서 점수를 구하면 된다.
from collections import deque

n = int(input())
graph = []
s_size = 2
s_x, s_y = 0, 0
result = 0
# 공간 입력 받기
for i in range(n):
  data = list(map(int, input().split()))
  graph.append(data)

# 먹을 수 있는 물고기가 2마리 이상일때
# 주변으로 이동했을떄 타겟팅한 물고기와의 위치를 연산해서 최솟값을 나타내는 부분을 찾아야함

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

while True:
  count = 0 # 먹을 수 있는 물고기 몇마리
  eated = 0 # 물고기 몇마리 먹었는지
  eat = []
  for i in range(n):
    for j in range(n):
      if 0 < graph[i][j] < s_size:
        count += 1
        eat.append((i, j))
      if graph[i][j] == 9:
        s_x, s_y = i, j # 상어 위치 

  eat.sort()
  if count == 0:
    break
  
  else:
    temp = 0 # 몇칸 이동했는지
    visited = [[False]*n for _ in range(n)] # 방문했는지
    t_x, t_y = eat[0] # 먹을 물고기의 위치
    q = deque()
    q.append((s_x, s_y, temp))
    visited[s_x][s_y] = True

    while q:
      x, y, temp = q.popleft() # 상어의 현재 위치

      if (x, y) == (t_x, t_y): # 물고기의 위치 일 경우
        result += temp 
        eated += 1
        if eated == s_size: # 레벨업(크기 증가)
          eated = 0
          s_size += 1
        break
      # 상하좌우 살피기
      for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
          if graph[nx][ny] <= s_size: # 물고기의 크기가 상어랑 사이즈가 동일하거나 작으면 이동가능
            q.append((nx, ny, temp+1))
            visited[nx][ny] = True          
    
print(result)
      

  # 상어가 먹을 수 있는 물고기 위치, 갯수 카운트

# 상어의 크기, result(이동한 칸의 갯수), 이동명령, 먹을 수 있는 상어의 갯수(위치), 현재위치
# 이동하는 방법, 거리 구하기(최솟값),

    
    
  