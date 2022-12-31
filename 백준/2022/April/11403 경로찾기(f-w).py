n = int(input())
graph = []
for i in range(n):
    data = list(map(int, input().split()))
    graph.append(data)

for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][k] and graph[k][j]: #k를 거쳐 가는 길이 있으면 경로가 있는 것
                graph[i][j] = 1

for i in range(n):
    for j in range(n):
        print(graph[i][j], end=' ')
    print()