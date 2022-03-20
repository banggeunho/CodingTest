# 백준 18353 병사배치하기
n = int(input())
arr = list(map(int, input().split()))
arr.reverse()
dp = [1]*n
for i in range(n):
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(n - max(dp))