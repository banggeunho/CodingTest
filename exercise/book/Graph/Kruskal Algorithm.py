# 코딩테스트 대비 기초 문제 풀이 23일차
# Date : 2022. 02. 09.
# Graph Algorithm


# <신장 트리 : Spanning Tree>
# 하나의 그래프가 있을 때 모든 노드를 포함하면서 사이클이 존재하지 않는 부분 그래프

# <크루스칼 알고리즘 Kruskal Algorithm> : 최소 신장 트리 알고리즘
# 신장 트리 중에서 최소 비용으로 만들 수 있는 신장트리를 찾는 알고리즘
# 그리디 알고리즘으로 분류된다.

# 모든 간선에 대하여 정렬을 수행한 뒤에 가장 거리가 짧은 간선부터 집합에 포함시키면 된다.
# 이떄 사이클을 발생시킬 수 있는 간선의 경우, 집합에 포함시키지 않는다.

# 시간 복잡도 : O(ElogE) // 간선의 개수 : E

# <크루스칼 알고리즘>
# 1. 간선 데이터를 비용에 따라 오름차순으로 정렬한다.
# 2. 간선을 하나씩 확인하며 현재의 간선이 사이클을 발생시키는지 확인한다.
#   - 1) 간선 데이터를 비용에 따라 오름차순으로 정렬한다.
#   - 2) 사이클이 발생하는 경우 최소 신장 트리에 포함시키지 않는다.
# 3. 모든 간선에 대하여 2번의 과정을 반복한다.


# 크루수칼 알고리즘

# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
  # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)

  # 루트노드의 번호가 더 작은 것으로 바궈줌
  if a < b:
    parent[b] = a
  else:
    parent[a] = b

# 노드와 개수와 간선*(union 연산)의 개수 입력 받기
v, e = map(int, input().split())
parent = [0] * (v + 1) # 부모 테이블 초기화

edges = []
result = 0

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v+1):
  parent[i] = i

# union 연산을 각각 수행
for i in range(e):
  a, b, cost = map(int, input().split())
  edges.append((cost, a, b))

# 간선을 비용순으로 정렬
edges.sort()

# 간선을 하나씩 확인하며
for edge in edges:
  cost, a, b = edge
  # 사이클이 발생하지 않는 경우에만 집합에 포함
  if find_parent(parent, a) != find_parent(parent, b):
    union_parent(parent, a, b)
    result += cost

print(result)