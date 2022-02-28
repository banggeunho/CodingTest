# 코딩테스트 대비 기초 문제 풀이 40일차
# Date : 2022. 02. 28.
# 구현 문제 풀이

#-------------------------****----------------------------------
# N의 범위가 500인 경우 : 시간 복잡도가 O(N^3)인 알고리즘을 설계
# N의 범위가 2,000인 경우 : 시간 복잡도가 O(N^2)인 알고리즘을 설계
# N의 범위가 100,000인 경우 : 시간 복잡도가 O(NlogN)인 알고리즘을 설계
# N의 범위가 10,000,000인 경우 : 시간 복잡도가 O(N)인 알고리즘을 설계
#-------------------------****----------------------------------


# BFS 예제
from collections import deque

n, m ,k, x = map(int, input().split())
# 인접 리스트 예제

graph = [[] for _ in range(n+1)]
for i in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  
distance = [-1]*(n+1)
distance[x] = 0
# BFS(Breadth-First-Search) : 너비 우선 탐색, 가까운 노드부터 탐색하는 알고리즘

# BFS 메서드 정의
q = deque([x])
while q:
  now = q.popleft()
  for next_node in graph[now]:
    # 방문하지 않은 노드
    if distance[next_node] == -1:
      distance[next_node] = distance[now] + 1
      q.append(next_node)


check = False
for i in range(1, n+1):
  if distance[i]==k:
    print(i)
    check = True

if not check:
  print(-1)

