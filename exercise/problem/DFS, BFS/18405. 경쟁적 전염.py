# 코딩테스트 대비 기초 문제 풀이 40일차
# Date : 2022. 03. 02.
# 구현 문제 풀이
# https://www.acmicpc.net/problem/14502
#-------------------------****----------------------------------
# N의 범위가 500인 경우 : 시간 복잡도가 O(N^3)인 알고리즘을 설계
# N의 범위가 2,000인 경우 : 시간 복잡도가 O(N^2)인 알고리즘을 설계
# N의 범위가 100,000인 경우 : 시간 복잡도가 O(NlogN)인 알고리즘을 설계
# N의 범위가 10,000,000인 경우 : 시간 복잡도가 O(N)인 알고리즘을 설계
#-------------------------****----------------------------------

from collections import deque
# arr 범위, 바이러스 종류 입력 받기
N, K = map(int, input().split())
arr = []
graph = [[]*i for i in range(K+1)]
for i in range(N):
    arr.append(list(map(int, input().split())))
    for j in range(N):
      if arr[i][j] != 0:
        graph[arr[i][j]].append((i, j))

  
s, x, y = map(int, input().split())

dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]

# s초가 지난다.
for i in range(s):
  temp = [[]*i for i in range(K+1)]
  for j in range(1, K+1):
    q = deque([j])
    while q:
      now = q.popleft()
      # print(now)
      for cx, cy in graph[now]:
        # graph[now].remove((cx, cy))
        
        # 상하좌우 살피기
        for k in range(4):
          nx = cx + dx[k]
          ny = cy + dy[k]

          if 0<= nx < N and 0 <= ny < N:
            if arr[nx][ny] == 0:
              arr[nx][ny] = now
              temp[now].append((nx, ny))
  # print(arr)
  graph = temp
  # print(graph)
# print(arr)
print(arr[x-1][y-1])
      
        
    



  
    

  
  