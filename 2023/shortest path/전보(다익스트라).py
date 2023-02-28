import heapq
import sys
INF = int(1e9)
input = sys.stdin.readline

n, m, start = map(int, input().split())
graph = [[] for i in range(n+1)]
distance = [INF] * (n + 1)

for i in range(m):
    x, y, cost = map(int, input().split())
    graph[x].append((y, cost))

def dijikstra(start):
    q = []
    heapq.heappush(q, (0, start)) # q에 현재 노드 추가
    distance[start] = 0 # 출발지는 0으로 갱신

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijikstra(start)
result_count = 0
max_distance = 0
for d in distance:
    if d != INF:
        max_distance = max(max_distance, d)
        result_count += 1

print(result_count - 1, max_distance)


print(n, m, start)
print(graph)
print(distance)

# 3 2 1
# 1 2 4
# 1 3 2