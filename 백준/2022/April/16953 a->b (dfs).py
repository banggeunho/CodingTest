from collections import deque
a, b = map(int, input().split())

q = deque()
q.append((a, 0))

result = int(1e9)+1

def dfs(now, cost):
    global result
    if now == b:
        result = min(result, cost)

    if now > b:
        return

    dfs(now*2, cost+1)
    dfs(now*10+1, cost+1)

dfs(a, 1)
print(-1 if result == int(1e9)+1 else result)










