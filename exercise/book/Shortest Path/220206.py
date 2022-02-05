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

# [방법 1] 다익스트라 // 시간복잡도 : O(V^2) V는 노드이 개수
# * 모든 리스트는 (노드의 개수 + 1) -> 노드의 번호를 인덱스로 표현 :그래프를 표현해야  할 때 많이 사용하는 일반적인 코드 작성법

import sys
input = sys.stdin.readline
INF = int(1e9)

# 노드의 개수, 간선의 개수를 입력받기
n, m = map(int, input().split())
# 시작 노드 번호 입력받기
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for i in range(n+1)]
# 방문한 적이 있는지 체크하는 목적의 리스트를 만들기
visited = [False] * (n+1)
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n+1)

# 모든 간선 정보를 입력받기
for _ in range(m):
  a, b, c = map(int, input().split())
  # a 번 노드에서 b번 노드로 가는 비용이 c이다.
  graph[a].append((b,c))

# 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 변환
def get_smallest_node():
  min_value = INF
  index = 0 # 가장 최단 거리가 짧은 노드(인덱스)
  for i in range(1, n+1):
    if distance[i] < min_value and not visited[i]:
      min_value = distance[i]
      index = i

  return index

def dijkstra(start):
  # 시작 노드에 대해서 초기화
  distance[start] = 0
  visited[start] = True
  for j in graph[start]:
    distance[j[0]] = j[1]

  # 시작 노드를 제외한 전체 n-1개의 노드에 대해 반복
  for i in range(n-1):
    # 현재 최단 거리가 가장 짧은 노드를 꺼내서, 방문 처리
    now = get_smallest_node()
    visited[now] = True
    # 현재 노드와 연결된 다른 노드를 확인
    for j in graph[now]:
      cost = distance[now] + j[1]
      # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
      if cost < distance[j[0]]:
        distance[j[0]] = cost

dijkstra(start)

for i in range(1, n+1):
  if distance[i] == INF:
    print('INFINITY')
  else:
    print(distance[i])




# [방법 2] 개선된 다익스트라 // 시간복잡도 : O(ElogV)) V는 노드이 개수, E는 간선의 개수