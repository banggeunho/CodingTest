# https://www.acmicpc.net/problem/14501
N = int(input())
schedule = [list(map(int, input().split())) for i in range(N)]
dp = [0 for _ in range(N+1)] # i일까지 얻을 수 있는 최대 수익 저장

for i in range(N):
    for j in range(i + schedule[i][0], N+1):
        if dp[j] < dp[i] + schedule[i][1]:
            dp[j] = dp[i] + schedule[i][1]
        # print(dp)

print(dp[-1])
