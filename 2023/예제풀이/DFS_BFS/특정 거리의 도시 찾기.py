from collections import deque

n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n + 1)]
distance = [-1] * (n + 1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b) # 목적지

def bfs(graph, start, distance):
    q = deque([start])
    distance[start] = 0

    while q:
        now = q.popleft()

        for i in graph[now]:
            if distance[i] == -1:
                q.append(i)
                distance[i] = distance[now] + 1

    return distance

result = bfs(graph, x, distance)
solve = False
for i in range(1, n+1):
    if distance[i] == k: # 최단 거리를 가진 노드
        print(i)
        solve = True

if not solve:
    print(-1)