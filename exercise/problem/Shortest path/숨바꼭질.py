# 코딩테스트 대비 기초 문제 풀이 
# Date : 2022. 03. 22.
# Shortest path
#-------------------------****----------------------------------
# N의 범위가 500인 경우 : 시간 복잡도가 O(N^3)인 알고리즘을 설계
# N의 범위가 2,000인 경우 : 시간 복잡도가 O(N^2)인 알고리즘을 설계
# N의 범위가 100,000인 경우 : 시간 복잡도가 O(NlogN)인 알고리즘을 설계
# N의 범위가 10,000,000인 경우 : 시간 복잡도가 O(N)인 알고리즘을 설계
#-------------------------****------------------------------------


# 숨바꼭질 ( 다익스트라 알고리즘 활용, bfs를 이용해서도 풀이 가능)
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

# 가장 멀리 떨어진 곳 찾아라
max_dist = 0
for i in range(1, n+1):
    max_dist = max(max_dist, distance[i])

# 갯수와 인덱스 위치를 알아야하기 떄문에 한번 더 loop
count = 0
save_zone = []
for i in range(1, n+1):
    if max_dist == distance[i]:
        count += 1
        save_zone.append(i)

print(f'{save_zone[0]} {distance[save_zone[0]]} {len(save_zone)}')