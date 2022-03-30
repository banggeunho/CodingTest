# 인프런 미로탐색 문제
# dfs로 풀면서 방문 list를 주어 푸는 것이 포인트
# dfs보내고 다시 그 부분은 false로 처리해주어 각각의 방문 list를 갖도록 설정

import sys
sys.setrecursionlimit(10**5)

arr = []
for _ in range(7):
    arr.append(list(map(int, input().split())))

# 방문 처리 list 시작점 True 초기화
visited = [[False]*7 for _ in range(7)]
visited[0][0] = True

# 상하좌우
dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]

result = 0
def dfs(x, y, visited):
    global arr, result
    
    # 도착했을때~
    if x==6 and y==6:
        result += 1

    # 벽임신
    if arr[x][y] == 1:
        return
    
    # 훙냥냥 스킬
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < 7 and 0 <= ny < 7 and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny, visited)
            visited[nx][ny] = False

dfs(0, 0, visited)
print(result)