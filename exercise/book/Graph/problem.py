# 코딩테스트 대비 기초 문제 풀이 24일차
# Date : 2022. 02. 10.
# 그래프 문제 풀이

# 팀 결성

# 학생들은 0번부터 N번까지의 번호
# 모든 학생이 서로 다른 팀으로 구분되어, 총 N+1개의 팀이 존재한다.

# '팀 합치기', '같은 팀 여부 확인'연산 사용 가능

# 1. 팀 합치기 연산은 두 팀을 합치는 연산
# 2. 같은 팀 여부 확인 연산은 특정한 두 학생이 같은 팀에 속하는지를 확인하는 연산이다.

# 팀 합치기 연산은 0 A B 형태로 주어진다. 이는 A번 학생이 속한 팀과 B번 학생이 속한 팀을 합친다는 의미.
# 같은 팀 여부 확인 연산은 1 A B 형태로 주어진다. 이는 A번 학생과 B번 학생이 같은 팀에 속해 있는 지를 확인하는 연산.
# a, b는 N 이하의 양의 정수이다.
# 같은 팀 여부 확인 연산에 대하여 한 줄에 하나씩 yes 혹은 no로 결과를 출력한다.

# -> 서로소 집합을 이용하여 푸는 문제!


# 개선된 서로소 집합 알고리즘 소스코드  
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


n, m = map(int, input().split())
parent = [0] * (n + 1) # 부모 테이블 초기화

for i in range(1, n+1):
  parent[i] = i

for _ in range(m):
  c, a, b = map(int, input().split())

  if c == 0: # 합치기
    union_parent(parent, a, b)
  
  if c == 1: # 같은 팀 여부 확인
    if find_parent(parent, a) == find_parent(parent, b):
      print('YES')
    else:
      print('NO')


# 도시 분할 계획

# 마을은 n개의 집과 연결하는 m개의 길, 방향성은 없음
# 길마다 유지비가 있음 -> 간선에 비용이 있다.

# 마을을 2개의 분리돈 마을로 분할할 계획을 세우고 있다.
# 마을을 분할할 때는 각 분리된 마을 안에 집들이 서로 연결되도록 분할해야함
# 두 집 사이에 경로가 항상 존재해야 한다. 마을에는 집이 하나 이상 있어야 함

# 분리된 두 마을 사이에 있는 길들은 필요가 없어 없앨 수 있다.
# 최소 비용으로 길을 놓고 싶다.

# N은 2 이상 10만 이하인 정수, m은 1 이상 백만이하인 ㅓㅈㅇ수
# a, b, c : a와 b를 연결하는 길의 유지비는 c

# 전체 그래프에서 2개의 최소 신장 트리를 만들어야 하는 것
# 크루스칼 알고리즘으로 최소 신장 트리를 찾은 뒤에 최소 신장 트리를 구성하는 간선 중에서 가장 비용이 큰 간선을 제거하는 것이다,.

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
n, m = map(int, input().split())
parent = [0] * (n + 1) # 부모 테이블 초기화

edges = []
result = 0

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, n+1):
  parent[i] = i

# union 연산을 각각 수행
for i in range(m):
  a, b, cost = map(int, input().split())
  edges.append((cost, a, b))

# 간선을 비용순으로 정렬
edges.sort()
max_cost = 0
# 간선을 하나씩 확인하며
for edge in edges:
  cost, a, b = edge
  # 사이클이 발생하지 않는 경우에만 집합에 포함
  if find_parent(parent, a) != find_parent(parent, b):
    union_parent(parent, a, b)
    if max_cost < cost:
      max_cost = cost
    result += cost

print(result-max_cost)

# 커리큘럼

# queue 자료 구조를 이용하기 위한 deque 라이브러리 활용
from collections import deque
import copy

# 노드의 개수와 간선의 개수를 입력받기
v = int(input())
# 모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0] * (v+1)
# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트(그래프) 초기화
graph = [[] for i in range(v + 1)]
# 각 강의 시간을 0으로 초기화
time = [0] * (v+1)

# 방향 그래프의 모든 간성 정보를 입력받기
for i in range(1, v+1):
  data = list(map(int, input().split()))
  time[i] = data[0] # 첫번째 수는 시간 정보를 담고 있음
  for x in data[1:-1]: # 두번째 부터 마지막 전까지는 선수 강의를 갖고 있음. 진입 차수 추가
    indegree[i] += 1
    graph[x].append(i)

# 위상 정렬 함수
def topology_sort():
  result = copy.deepcopy(time) # 알고리즘 수행 결과를 담을 리스트
  q = deque() # 큐 기능을 위한 deque 라이브러리 사용

  # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
  for i in range(1, v+1):
    if indegree[i] == 0:
      q.append(i)
  
  # 큐가 빌 때까지 반복
  while q:
    # 큐에서 원소 꺼내기
    now = q.popleft()

    # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
    for i in graph[now]:
      # 인접한 노드의 시간과 현재 노드와 인접한 노드의 시간의 합 중 더 큰 것을 result로 갱신
      result[i] = max(result[i], result[now] + time[i])
      print(now, i, result[i])
      indegree[i] -= 1
      # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
      if indegree[i] == 0:
        q.append(i)
  
  # 위상 정렬을 수행한 결과 출력
  for i in range(1, v+1):
    print(result[i])

topology_sort()