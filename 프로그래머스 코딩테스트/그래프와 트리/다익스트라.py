import heapq
import sys

input = sys.stdin.readline
INF = float('inf')
n, m = map(int, input().split())
start = int(input())
# 그래프와 거리 리스트 초기화
graph = [[] for i in range(n+1)]
distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split()) # a -> b : c
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    # 자기 자신(시작 노드)로 가는 최단 경로는 0
    # 비용을 앞에 넣는 이유는 비용이 저렴한 순으로 나오게 하기 위해
    heapq.heappush(0, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        # 거리 노드에 이미 짧은 거리가 존재할 경우 skip
        if distance[now] < dist:
            continue

        # 현재 연결된 노드들을 탐색하면서
        for i in graph[now]:
            cost = dist + i[1] # 지금 거리와, 대상 노드까지의 거리를 합하고
            if cost < distance[i[0]]: # 그 비용이, 현재 거리 노드에 있는 값보다 저렴할 경우
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0])) # 큐에 추가한다 비용과 해당 지점을

# 다익스트라 알고리즘으로
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n+1):
  # 도달할 수 없는 경우, 무한(infinity)이라고 출력
  if distance[i] == INF:
    print('INFINITY')
  else:
    print(distance[i])