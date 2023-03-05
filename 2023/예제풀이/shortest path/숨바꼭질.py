import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int , input().split())

# 그래프와 거리 list 초기화
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

# 양방향 연결 (거리는 길의 갯수이므로 1로 두었음)
for _ in range (m):
    a, b = map(int, input().split())
    graph[a].append((b, 1))
    graph[b].append((a, 1))


# 우선순위 큐를 활용한 다익스트라 알고리즘, 출발 지점은 항상 1
q = []
# 거리, 위치
heapq.heappush(q, (0, 1))
distance[1] = 0

while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
        continue
    for i in graph[now]:
        cost = dist + i[1]
        if cost < distance[i[0]]:
            heapq.heappush(q, (cost, i[0]))
            distance[i[0]] = cost

result_idx = distance.index(max(distance[1:]))
result_dis = distance[result_idx]
result_cnt = distance.count(distance[result_idx])

print(result_idx, result_dis, result_cnt)