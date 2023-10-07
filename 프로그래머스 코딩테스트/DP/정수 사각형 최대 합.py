n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * (n) for _ in range(n)]
dp[0][0] = data[0][0]
for i in range(1, n):
    dp[0][i] = dp[0][i - 1] + data[0][i]
    dp[i][0] = dp[i - 1][0] + data[i][0]

for i in range(1, n):
    for j in range(1, n):
        dp[i][j] = max(dp[i - 1][j] + data[i][j], dp[i][j - 1] + data[i][j])

print(dp[n - 1][n - 1])