import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)

def dfs(u, visited):
    visited.add(u)
    checked[u] = 1
    for v in g[u]:
        if v not in visited: # 이미 방문한 노드가 뽑히면 사이클이 생기는 것
            dfs(v, visited.copy())
        else:
            # 사이클이 생기면 뽑는다.
            result.extend(list(visited))
            return

n = int(sys.stdin.readline().strip())
g = defaultdict(list)
for i in range(1, n+1):
    v = int(sys.stdin.readline().strip())
    g[v].append(i)

print(g)
checked = [0 for _ in range(n+1)]
result = []
for i in range(1, n+1):
    if not checked[i]:
        dfs(i, set([]))
        result.sort()


print(len(result))
for x in result:
    print(x)
