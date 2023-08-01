# https://school.programmers.co.kr/learn/courses/30/lessons/42898
def dfs(x, y, dp, puddles):
    row, col = len(dp), len(dp[0])
    path = [[1, 0], [0, 1]]

    if [x, y] == [row -1, col -1]: return 1 # 도착지인 경우 +1 반환
    if dp[x][y] != 0: return dp[x][y] # 누가 지나갔을 경우 현재 경우의 수를 반환

    for i in range(2):
        nx = x + path[i][0]
        ny = y + path[i][1]

        if 0 <= nx < row and 0 <= ny < col:
            if [ny + 1, nx + 1] in puddles: continue
            dp[x][y] += dfs(nx, ny, dp, puddles) # 누적합

    return dp[x][y] % 1000000007

def solution(m, n, puddles):
    dp = [[0] * m for _ in range(n)]
    return dfs(0, 0, dp, puddles)

print(solution(4, 3, [[2, 2]]))

from collections import deque

def solution(m, n, puddles):
    dp = [[0] * m for _ in range(n)]
    path = [(1, 0), (0, 1)]

    dp[0][0] = 1  # Start point

    queue = deque([(0, 0)])

    while queue:
        x, y = queue.popleft()

        for dx, dy in path:
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < m:
                if [ny + 1, nx + 1] not in puddles:
                    if dp[nx][ny] == 0: # 누가 안 지나갔으면 내 경우의 수로 덮어씌기
                        dp[nx][ny] = dp[x][y]
                        queue.append((nx, ny))
                    else: # 기존에 누가 지나갔으면 내 것도 더하기
                        dp[nx][ny] = (dp[nx][ny] + dp[x][y])

    return dp[n-1][m-1] % 1000000007


def solution(m, n, puddles):
    dp = [[0] * m for _ in range(n)]
    dp[0][0] = 1

    for x in range(n):
        for y in range(m):
            if ([y + 1, x + 1] in puddles) or ((x, y) == (0, 0)): continue
            # 위에서 올 경우, 왼쪽에서 올경우 두가지 경우를 더한다.
            dp[x][y] = (dp[x - 1][y] + dp[x][y - 1]) % 1000000007

    return dp[-1][-1]