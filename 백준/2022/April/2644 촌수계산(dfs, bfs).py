# https://www.acmicpc.net/problem/2644
def dfs(now):
    for i in graph[now]:
        if visited[i] == 0:
            visited[i] = visited[now]+1
            dfs(i)

def bfs(now):
    from collections import deque
    q = deque()
    q.append(now)

    while q:
        now = q.popleft()
        for i in graph[now]:
            if visited[i] == 0:
                visited[i] = visited[now]+1
                q.append(i)

n = int(input())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
p, s = map(int, input().split())
m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# dfs(s)
bfs(s)
print(visited[p] if visited[p] > 0 else -1)