
# 코딩테스트 대비 기초 문제 풀이 
# Date : 2022. 04. 3.
# 삼성전자 기출 문제
#-------------------------****----------------------------------
# N의 범위가 500인 경우 : 시간 복잡도가 O(N^3)인 알고리즘을 설계
# N의 범위가 2,000인 경우 : 시간 복잡도가 O(N^2)인 알고리즘을 설계
# N의 범위가 100,000인 경우 : 시간 복잡도가 O(NlogN)인 알고리즘을 설계
# N의 범위가 10,000,000인 경우 : 시간 복잡도가 O(N)인 알고리즘을 설계
#-------------------------****------------------------------------

from collections import deque
m, n, h = map(int, input().split())
arr = [[] for _ in range(h)]
cnt = 0
for i in range(h):
    for j in range(n):
        arr[i].append(list(map(int, input().split())))

# print(arr)
# print(arr[0][2][4]) # 맨 윗층 에서 맨 마지막 원소 출력

dx = [0, 0, 0, 0, -1, 1]
dy = [0, 0, -1, 1, 0, 0]
dh = [-1, 1, 0, 0, 0, 0]

while True:
    cnt += 1
    # 종료 조건
    visited = [[False]*m for _ in range(n)] * h
    print(visited)
    # print(cnt, visited[0][0])
    q = deque()
    q.append((0, 0, 0)) # x, y, h
    visited[0][0] = True
    while q:
        x, y, h = q.popleft()
        if arr[h][x][y] == 1:
            for i in range(6):
                nx, ny, nh = x+dx[i], y+dy[i], h+dh[i]
                if 0 <= nx < n and 0 <= ny < m and 0 <= nh < h and arr[nh][nx][ny] == 0 and not visited[nh][nx][ny]: # 범위 안에 있을때
                    q.append((nx, ny, nh))
                    arr[nh][nx][ny] = 1
                    visited[nh][nx][ny] = True
            