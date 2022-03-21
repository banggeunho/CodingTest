#11404 플로이드 (백준)
n = int(input())
m = int(input())
INF = int(1e9)
graph = [[INF]*(n+1) for _ in range(n+1)]
for _ in range(m):
  a, b, c = map(int, input().split())
  # 노선이 하나가 아닐 수도 있음.
  graph[a][b] = min(graph[a][b], c)

# floyd-warshall algorithm
for k in range(1, n+1):
# 출발 지점과 도착 지점이 같은 곳은 0으로 초기화
  graph[k][k] = 0
  for i in range(1, n+1):
    for j in range(1, n+1):
        graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

# 결과 출력
for i in range(1, n+1):
  for j in range(1, n+1):
    if graph[i][j] == INF:
      graph[i][j] = 0
    print(graph[i][j], end=' ')
  print()