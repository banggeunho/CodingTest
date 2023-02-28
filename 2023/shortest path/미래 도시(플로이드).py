INF = int(1e9)

# 노드, 간선 개수 정보 입력 받기
n, m = map(int, input().split())

# 2차원 리스트(그래프 표현)을 만들고, 모든 값을 무한으로 초기화
graph = [[INF] * (n + 1) for _ in range(n+1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(m):
    # A에서 B로 가는 비용은 C라고 설정
    a, b = map(int, input().split())
    # 양방향으로 이동 가능
    graph[a][b] = 1
    graph[b][a] = 1

# x (목적지), k(소개팅 장소)
x, k = map(int, input().split())

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])


result = graph[1][k] + graph[k][x]

if result > INF:
    print(-1)
else:
    print(result)


# 5 7
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4
# 3 5
# 4 5
# 4 5

# ---
# 4 2
# 1 3
# 2 4
# 3 4
