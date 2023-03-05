
import heapq
import sys

INF = int(1e9)
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for tc in range(1, int(input()) + 1):
    n = int(input())
    graph = []
    for _ in range(n):
        graph.append(list(map(int, input().split())))

    distance = [[INF] * n for _ in range(n)]

    q = []
    heapq.heappush(q, (graph[0][0], 0, 0))
    distance[0][0] = graph[0][0]

    while q:
        energy, x, y = heapq.heappop(q)

        if distance[x][y] < energy:
            continue

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                cost = energy + graph[nx][ny]
                if cost < distance[nx][ny]:
                    heapq.heappush(q, (cost, nx, ny))
                    distance[nx][ny] = cost

    print(distance[n-1][n-1])

