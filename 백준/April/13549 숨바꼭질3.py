
# *2 의 위치로 움직이는 텔레포트가 많아야 빨리 도착 비용도 안들기때문에
# 그래서 q.appendleft로 추가해주는게 이득임

from collections import deque
n, k = map(int, input().split())
visited = [0]*100001

q = deque()
q.append(n)
visited[n] = 1
while q:
    now = q.popleft()

    if now == k:
        break

    if 0 <= now * 2 < 100001 and not visited[now * 2]:
        q.appendleft(now*2)
        visited[now*2] = visited[now]

    if 0 <= now+1 < 100001 and not visited[now+1]:
        q.append(now+1)
        visited[now+1] = visited[now] + 1

    if 0 <= now-1 < 100001 and not visited[now-1]:
        q.append(now-1)
        visited[now-1] = visited[now] + 1

print(visited[k]-1)