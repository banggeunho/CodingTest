# 코딩테스트 대비 기초 문제 풀이 
# Date : 2022. 03. 07.
# 구현 문제 풀이
# https://www.acmicpc.net/problem/14888
#-------------------------****----------------------------------
# N의 범위가 500인 경우 : 시간 복잡도가 O(N^3)인 알고리즘을 설계
# N의 범위가 2,000인 경우 : 시간 복잡도가 O(N^2)인 알고리즘을 설계
# N의 범위가 100,000인 경우 : 시간 복잡도가 O(NlogN)인 알고리즘을 설계
# N의 범위가 10,000,000인 경우 : 시간 복잡도가 O(N)인 알고리즘을 설계
#-------------------------****----------------------------------
# 연합은 여러개 만들어질 수 있으며, 연합마다 인덱스를 넣어주어 이게 처리되었는지 확인을 하는게 핵심이다.
# 연합에 먼저 들어가게되면 거기에 맞게 평균을 구해 인구를 바꿔준다.
# 연합이 들어가지 않은 부분만 함수를 실행하여 처리를 해주고
# 전체 각자 다른 연합에 들어갈때까지 함수를 돌리면 된다.

from collections import deque

n, l, r = map(int, input().split())

graph =[]
for _ in range(n):
  graph.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

result = 0

def process(x, y, index, union):
  # (x,y)의 위치와 연결된 나라(연합) 정보를 담는 리스트
  united = []
  united.append((x, y))
  # 너비 우선 탐색을 위한 큐 자료구조 정의
  q = deque()
  q.append((x,y))

  # 현재 연합의 번호 할당
  union[x][y] = index
  # 현재 연합의 전체 인구수
  summary = graph[x][y]
  count = 1
  # 큐가 빌 때까지 반복
  while q:
    x, y = q.popleft()
    # 현재 위치에서 4가지 방향을 확인
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      # 바로 옆에 있는 나라를 확인
      if 0 <= nx < n and 0 <= ny < n and union[nx][ny] == -1:
        # 옆에 있는 나라와 인구 차이 확인
        if l <= abs(graph[nx][ny] - graph[x][y]) <= r:
          q.append((nx, ny))
          # 연합에 추가
          union[nx][ny] = index
          summary += graph[nx][ny]
          count += 1
          united.append((nx, ny))
  # 연합 국가끼리 인구를 분배
  for i, j in united:
    graph[i][j] = summary // count

  return count

total_count = 0
  
while True:
  union = [[-1]*n for _ in range(n)]
  index = 0
  for i in range(n):
    for j in range(n):
      if union[i][j] == -1:
        process(i, j, index, union)
        index += 1
          
  # 모든 인구 이동이 끝난 경우(2중 for문이 모두 돌아간거면 인구이동 x)
  if index == n * n:
    break
  total_count += 1
    
print(total_count)