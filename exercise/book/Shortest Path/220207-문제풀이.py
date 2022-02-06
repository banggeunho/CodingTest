# 코딩테스트 대비 기초 문제 풀이 21일차
# Date : 2022. 02. 06.
# 최단경로 문제 풀이

# 미래도시
# 방문판매원이 소개팅을 참석하고, 최종적으로 회사에 가는 최단 경로를 구하여라

# 소스코드
INF = int(1e9)
n, m = map(int, input().split())

# 2차원 리스트(그래프 표현)을 만들고, 모든 값을 무한으로 초기화.
graph = [[INF]*(n+1) for _ in range(n+1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n+1):
  for b in range(1, n+1):
    if a == b:
      graph[a][b] = 0

# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(m):
  # 서로 양방향으로 연결 되어있음, 거리는 1
  a, b = map(int, input().split())
  graph[a][b] = 1
  graph[b][a] = 1
x, k = map(int, input().split())

# 점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(1, n+1):
  for a in range(1, n+1):
    for b in range(1, n+1):
      graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

distance = graph[1][k] + graph[k][x]

if distance >= INF:
  print(-1)
else:
  print(distance)

# 전보
import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n, m, start = map(int, input().split())
graph = [[] for i in range(n+1)]
distance = [INF]*(n+1)

for _ in range(m):
  x, y, z = map(int, input().split())
  graph[x].append((y, z))

def dijkstra(start):
  q = []
  # 시작 노드로 가기 위한 최단 경로는 0으로 설정하며, 큐에 삽입
  heapq.heappush(q, (0, start))
  distance[start] = 0

  while q: # 큐가 비어있지 않다면
    # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
    dist, now = heapq.heappop(q)
    # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
    if distance[now] < dist:
      continue
    # 현재 노드와 연결된 다른 인접한 노드들을 확인
    for i in graph[now]:
      cost = dist + i[1]
      # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q,(cost, i[0]))

# 다익스트라 알고리즘
dijkstra(start)

city = [i for i in distance if i != INF and i != 0]
# print(city)
print(len(city), max(city))