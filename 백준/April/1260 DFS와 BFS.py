# 졸라 쉬움
from collections import deque
n, m, v = map(int, input().split())
graph = [[] for i in range(n+1)]
visited = [False] * (n+1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

print(graph)
def dfs(start):
    print(start, end = ' ')
    visited[start] = True
    # 조건 sorting 여러개 있을 경우 작은 번호부터
    for i in sorted(graph[start]):
        if not visited[i]:
            dfs(i)

def bfs(start):
    q = deque()
    visited = [False] * (n + 1)
    q.append(start)
    visited[start] = True

    while q:
        now = q.popleft()
        print(now, end = ' ')
        # 조건 sorting 여러개 있을 경우 작은 번호부터
        for i in sorted(graph[now]):
            if not visited[i]:
                q.append(i)
                visited[i] = True

dfs(v)
print()
bfs(v)