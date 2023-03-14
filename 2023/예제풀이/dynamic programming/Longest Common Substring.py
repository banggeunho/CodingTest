s1 = input()
s2 = input()

n, m = len(s1), len(s2)
length = max(n, m)

dp = [[0] * (m+1) for _ in range(n+1)]

result = 0
end_idx = (0, 0)
for i in range (n):
    for j in range(m):
        # 맨 첫번째 dp 리스트는 0으로 초기화
        if i == 0 or j == 0:
            dp[i][j] = 0

        # 문자가 같으면 왼쪽 위 자리를 보고 더하기 1
        if s1[i] == s2[j]:
            dp[i][j] = dp[i-1][j-1] + 1

        # 다르면 0으로 설정
        else:
            dp[i][j] = 0

        # 결과 갱신
        if result < dp[i][j]:
            end_idx = (i, j)
            result = max(result, dp[i][j])

result_str = []
for i in range(result):
    x, y = end_idx
    result_str.append(s2[y])
    end_idx = (x-1, y-1)

print(result)
print(''.join(result_str[::-1]))