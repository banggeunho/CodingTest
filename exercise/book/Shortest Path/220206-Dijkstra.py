# 코딩테스트 대비 기초 문제 풀이 21일차
# Date : 2022. 02. 06.
# 최단 경로(The Shortest Path) : 가장 짧은 경로를 찾는 알고리즘이다.

# 최단 경로 문제는 보통 그래프를 이용해 표현하는데 각 지점은 그래프에서 '노드(node)'로 표현되고, 지점간 연결된 도로는
# 그래프에서 '간선(Edge)'으로 표현된다.


# 다익스트라(dijkstra) 알고리즘은 그래프에서 여러 개의 노드가 있을 때, 특정한 노드에서 출발하여 다른 노드로 가는
# 각각의 최단 경로를 구해주는 알고리즘이다.

# 다익스트라 알고리즘은 '음의 간선'이 없을 때 정상적으로 동작한다. 
# 다익스트라 알고리즘은 기본적으로 그리디 알고리즘으로 분류돈다. 매번 '가장 작은 비용이 적은 노드'를 선택해서 임의의 과정을
# 반복하기 때문이다.

# 1. 출발 노드를 설정한다
# 2. 최단 거리 테이블을 초기화한다.
# 3. 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택한다.
# 4. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블을 갱신한다.
# 5. 위 과정에서 3번과 4번을 반복한다.

# 다익스트라 알고리즘은 최단경로를 구하는 과정에서 '각 노드에 대한 현재까지의 최단 거리' 정보를 항상 1차원 리스트에
# 저장하며 리스트를 계속 갱신한다는 특징이 있다.

# 매번 현재 철하고 있는 노드를 기준으로 주변 간선을 확인한다.

# 다익스트라 알고리즘을 구현하는 방법은 2가지이다.
# 방법 1. 구현하기 쉽지만 느리게 동작하는 코드
# 방법 2. 구현하기 어렵지만 빠르게 동작하는 코드


# [방법 2] 개선된 다익스트라 // 시간복잡도 : O(ElogV)) V는 노드이 개수, E는 간선의 개수

import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())
graph = [[] for i in range(n+1)]
distance = [INF]*(n+1)

for _ in range(m):
  a, b, c = map(int, input().split())
  graph[a].append((b, c))

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

# 다익스트라 알고리즘으로
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n+1):
  # 도달할 수 없는 경우, 무한(infinity)이라고 출력
  if distance[i] == INF:
    print('INFINITY')
  else:
    print(distance[i])


