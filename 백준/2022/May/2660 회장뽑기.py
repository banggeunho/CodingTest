from collections import deque
n = int(input())
graph = [[] for _ in range(n+1)]

# 입력 받기
while True:
    a, b = map(int, input().split())
    if a == -1 and b == -1:
        break
    graph[a].append(b)
    graph[b].append(a)

def bfs(now):
    visited = [False]*(n+1)
    q = deque()
    q.append((now, 0))
    visited[now] = True
    result = 0
    while q:
        now, cost = q.popleft()
        result = max(result, cost)
        for i in graph[now]:
            if not visited[i]:
                q.append((i, cost+1))
                visited[i] = True

    return result

scores = [100]
for i in range(1, n+1):
    scores.append(bfs(i))

print(min(scores), scores.count(min(scores)))
for i in range(1, n+1):
    if min(scores) == scores[i]:
        print(i, end=' ')
print()