# https://www.acmicpc.net/problem/1277
import heapq
def get_distance(a, b):
    x1, y1 = a
    x2, y2 = b
    return (abs(x1-x2)**2 + abs(y1-y2)**2)**0.5

N, W = map(int, input().split()) # 발전소 수, 전선의 수
M = float(input())

graph = [[] for _ in range(N + 1)]
pos = [[]]
for i in range(1, N + 1):
    x, y = map(int, input().split())
    pos.append((x, y))

for i in range(1, N + 1):
    for j in range(i + 1, N + 1):
        dist = get_distance(pos[i], pos[j])
        if dist <= M:
            graph[i].append((j, dist))
            graph[j].append((i, dist))

for _ in range(W):
    i, j = map(int, input().split())
    graph[i].append((j, 0))
    graph[j].append((i, 0))

INF = int(1e9)
distance = [INF] * (N + 1)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    return int(distance[N] * 1000)

print(dijkstra(1))
