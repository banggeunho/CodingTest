# BFS, DFS_BFS 뭘 써도 다 풀기 가능
# PARENT LIST 선언 후 PARENT가 지정 안되어있는 경우만 NODE 방문ㅇㅈ? ㅇㅈ
# 그래서 부모 채워준다 하나씩 다 채우면 끝
from collections import deque
q = deque()
n = int(input())
parent = [0]*(n+1)
arr = [[] for i in range(n+1)]
for i in range(n-1):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

parent[1] = 1
q.append(1)
while q:
    now = q.popleft()
    for i in arr[now]:
        if parent[i] == 0:
            parent[i] = now
            q.append(i)

for i in range(2, n+1):
    print(parent[i])
  