# 깊이만 생각했던 나.....
# 모든 해킹 가능한 컴퓨터 수를 구하는 것이므로
# 큐에 들어갈때마다 +1을 해줘야한다.........
# 각각 번호에서 이어지는 컴퓨터 수를 구해야하므로
# 각각의 번호에서 탐색을 해줘야함 -> visited도 계속 리셋

from collections import deque
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)

def bfs(x):
    result = 0
    visited = [False] * (n + 1)
    q = deque()
    q.append(x)
    visited[x] = True

    while q:
        now = q.popleft()
        for i in graph[now]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
                result += 1

    return result

results = []
for i in range(1, n+1):
    results.append(bfs(i))

answer = []
for i in range(n):
    if max(results) == results[i]:
        print(i+1, end=' ')