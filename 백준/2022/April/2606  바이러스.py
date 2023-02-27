# UNION-FIND(DISJOINT SET), 그래프 탐색, BFS 세가지 버전으로 문제 풀이
# 문제 풀이 시간은 셋 다 비슷하나 UNION-FIND < 그래프 탐색 < BFS 순으로 길어짐...

# UNION-FIND
def find_parent(x):
    global parent
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(a, b):
    global parent
    a = find_parent(a)
    b = find_parent(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


v = int(input())
e = int(input())
parent = [i for i in range(v+1)]
for _ in range(e):
    a, b = map(int, input().split())
    union_parent(a, b)

cnt = 0
for i in range(2, v+1):
    if find_parent(i) == find_parent(1):
        cnt+=1
print(cnt)



# 그래프 탐색
v = int(input())
e = int(input())
graph = [[] for _ in range(v+1)]
visited = [False]*(v+1)
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

count = -1
def dfs(start):
    global count
    now = start
    count += 1
    visited[now] = True

    for i in graph[now]:
        if not visited[i]:
            dfs(i)

dfs(1)
print(count)



# BFS
from collections import deque
v = int(input())
e = int(input())
graph = [[] for _ in range(v+1)]
visited = [False]*(v+1)
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

cnt = -1
q = deque()
q.append(1)
visited[1] = True

while q:
    now = q.popleft()
    cnt += 1
    for i in graph[now]:
        if not visited[i]:
            q.append(i)
            visited[i] = True

print(cnt)
