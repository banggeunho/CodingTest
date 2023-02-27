# 코딩테스트 대비 기초 문제 풀이 10일차
# Date : 2022. 01. 27.
# 자료구조(Data Structure)의 그래프 탐색/BFS를 이용한 기초 문제 풀이


# 그래프 탐색 동작원리 : 스택 // 구현 방법 : 재귀 함수 이용
# BFS 동작원리 : 큐 // 구현 방법 : 큐 자료구조 이용( 파이썬에서는 DEQUE 라이브러리 이용)

# 음료수 얼려 먹기 (예제) // 그래프 탐색 이용 문제 풀이, 상하좌우 위치의 DFS를 재귀적으로 호출하여 푸는게 핵심
n, m = map(int, input().split())

graph = []

for i in range(n):
  graph.append(list(map(int, input())))

def dfs(x, y):

  if x <= -1 or x >= n or y <= -1 or y >= m:
    return False
  
  # 노드를 아직 방문하지 않았다면
  if graph[x][y] == 0:
    
    # 방문 처리
    graph[x][y] = 1

    # 상하좌우 위치도 모두 재귀적으로 호출
    dfs(x - 1, y)
    dfs(x + 1, y)
    dfs(x, y - 1)
    dfs(x, y + 1)
    return True

  return False

result = 0
for i in range(n):
  for j in range(m):
    if dfs(i, j) == True:
      result += 1

print(result)


# 미로 탈출 (예제) // BFS 이용 문제 풀이, 출발점부터 BFS를 수행하여 모든 노드의 값을 거리 정보로 넣으면 된다.
# 특정한 노드를 방문하면 그 이전 노드의 거리에 1을 더한 값을 리스트에 넣는다.

from collections import deque

n, m = map(int, input().split())
graph = []
for i in range(n):
  graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
  queue = deque()
  queue.append(x, y)

  while queue:
    x, y = queue.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      # 지도에서 벗어난 경우
      if nx > 0 and nx <= n and ny > 0 and ny <= m:
        continue
      
      # 괴물이 있는 경우 (벽인 경우)
      if graph[nx][ny] == 0:
        continue

      # 이전 노드의 거리에 1을 더한 값을 리스트에 넣는다.
      if graph[nx][ny] == 1:
        graph[nx][ny] = graph[x][y] + 1
        queue.append((nx, ny))

  # 가장 오른쪽 아래까지의 최단 거리 변환
  return graph[n-1][m-1]

print(bfs(0,0))


