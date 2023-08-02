# 코딩테스트 대비 기초 문제 풀이 21일차
# Date : 2022. 02. 06.
# 최단 경로(The Shortest Path) : 가장 짧은 경로를 찾는 알고리즘이다.

# 최단 경로 문제는 보통 그래프를 이용해 표현하는데 각 지점은 그래프에서 '노드(node)'로 표현되고, 지점간 연결된 도로는
# 그래프에서 '간선(Edge)'으로 표현된다.


# 플로이드 워셜 알고리즘(Floyd-Warshall Alogorithm) : '모든 지점에서 다른 모든 지점까지의 최단 경로를 모두 구해야 하는 경우'에
# 사용할 수 있는 알고리즘이다.
# 시간 복잡도 : O(N^3)
# 점화식에 맞게 2차원 리스트를 갱신하기 때문에 다이나믹 프로그래밍으로 볼 수 있다.
# 점화식 : D(ab) = min(D(ab), D(ak)+D(kb))
# 'A에서 B로 가는 최소 비용'과 'A에서 K를 거쳐서 B로 가는 비용'을 비교하여 더 작은 값으로 갱신하겠다는 것이다,

# 소스코드
INF = int(1e9)
n = int(input())
m = int(input())

graph = [[INF] * (n + 1) for _ in range(n + 1)]

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if graph[a][b] == INF:
            print("INFINITY", end = ' ')
        else:
            print(graph[a][b], end = ' ')

    print()

