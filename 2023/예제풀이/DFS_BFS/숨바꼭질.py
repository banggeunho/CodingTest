from collections import deque

INF = int(1e9)
n, k = map(int, input().split())
visited = [INF] * 100001

q = deque()
q.append((n, 0))
visited[n] = 0
result = 0
while q:
    now, cost = q.popleft()

    if 0 <= now -1 <= 100000 and visited[now-1] > cost+1:
        q.append((now-1, cost+1))
        visited[now-1] = cost+1
    if 0 <= now + 1 <= 100000 and visited[now+1] > cost+1:
        q.append((now+1, cost+1))
        visited[now+1] = cost+1
    if 0 <= now * 2 <= 100000 and visited[now * 2] > cost+1:
        q.append((now*2, cost+1))
        visited[now*2] = cost+1

print(visited[k])