# 코딩테스트 대비 기초 문제 풀이 8일차
# Date : 2022. 01. 26.
# 자료구조(Data Structure)의 DFS/BFS를 위한 개념 공부


# 탐색 : 많은 양의 데이터 중에서 원하는 데이터를 찾는 과정
# 자료구조 : 데이터를 표현하고 관리하고 처리하기 위한 구조

# 스택(STACK) : 선입후출 구조 또는 후입선출 구조(First In Last Out))
# 예제 코드 ( list object의 appne와 pop을 이용해 구현 가능)

stack = []
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()

print(stack)
print(stack[::-1]) # 반대로 출력



# 큐(QUEUE) : 선입선출 구조(Last In Last Out), 공정한 자료구조
# 예제 코드 (dequeue 라이브러리 사용)

from collections import deque

queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.popleft()
queue.append(1)

print(queue)
queue.reverse() # 역순으로 바꾸기
print(queue)
print(list(queue)) # 리스트 형식을 바꾸기

# 재귀 함수(Recursive Function) : 자기 자신을 다시 호출하는 함수
# 예제 코드

def recursive_function(i):
  if i == 10:
    return
  print(i, end="")
  recursive_function(i+1)

recursive_function(1)
print('')

# 팩토리얼 예제(반복문 구현 + 재귀함수 구현)

# 반복문으로 구현
def factorial_iteration(n):
  result = 1
  for i in range(1, n+1):
    result *= i
  
  return result

# 재귀적으로 구현
def factorial_recursion(n):
  if n <=1:
    return 1
  return n*factorial_recursion(n-1)

print(factorial_iteration(5))
print(factorial_recursion(5))

# DFS(Depth-First-Search) : 깊이 우선 탐색, 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘

# 인접 행렬(Adjacancy Matrix) : 2차원 배열로 그래프의 연결 관계를 표현하는 방식
# 인접 리스트(Adjacancy List) : 리스트로 그래프의 연결 관계를 표현하는 방식

# 인접 행렬 예제
INF = 987654321

graph = [
  [0, 7, 5],
  [7, 0, INF],
  [5, INF, 0]
]

print(graph)

# 인접 리스트 예제
graph = [[] for _ in range(3)]

graph[0].append((1, 7))
graph[0].append((2, 5))

graph[1].append((0, 7))

graph[2].append((0, 5))

print(graph)


# DFS 예제
# DFS 메서드 정의
def dfs(graph, v, visited):
  # 현재 노드를 방문 처리
  visited[v] = True
  print(v, end=' ')

  # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
  for i in graph[v]:
    if not visited[i]:
      dfs(graph, i, visited)

graph = [
  [],
  [2, 3, 8],
  [1, 7],
  [1, 4, 5],
  [3, 5],
  [3, 4],
  [7],
  [2, 6, 8],
  [1, 7]
]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False] * 9

# 정의된 DFS 함수 호출
dfs(graph, 1, visited)
print('')

# BFS(Breadth-First-Search) : 너비 우선 탐색, 가까운 노드부터 탐색하는 알고리즘
# BFS 예제


# BFS 메서드 정의
def bfs(graph, start, visited):
  # 큐(Queue) 구현을 위해 deque 라이브러리 사용
  queue = deque([start])
  visited[start] = True

  while queue:
    v = queue.popleft()
    print(v, end=' ')
    # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True

# 각 노드가 연결된 정보를 리스트 자료형으로 표현 (2차원 리스트)
graph = [
  [],
  [2, 3, 8],
  [1, 7],
  [1, 4, 5],
  [3, 5],
  [3, 4],
  [7],
  [2, 6, 8],
  [1, 7]
]

visited = [False] * 9
bfs(graph, 1, visited)

# DFS 동작원리 : 스택 // 구현 방법 : 재귀 함수 이용
# BFS 동작원리 : 큐 // 구현 방법 : 큐 자료구조 이용( 파이썬에서는 DEQUE 라이브러리 이용)


    