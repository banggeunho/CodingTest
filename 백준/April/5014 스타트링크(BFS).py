# 5014 스타트 링크!!!!!
from collections import deque
F, S, G, U, D = map(int, input().split())
visited = [0]*(F+1)
q = deque()
q.append((S, 0))
visited[S] = 1
result = int(1e9)
while q:
    now, cost = q.popleft()
    if now == G:
        result = min(result, cost)

    if 1 <= now + U <= F:
        if visited[now+U] == 0:
            q.append((now + U, cost+1))
            visited[now + U] = cost + 1

    if 1 <= now - D <= F:
        if visited[now-D] == 0:
            q.append((now-D, cost + 1))
            visited[now - D] = cost + 1

print(result if result != int(1e9) else "use the stairs")