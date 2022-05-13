n = int(input())
m = int(input())
vip_chairs = []
dp = [0]*(n+1)
for i in range(m):
    vip_chairs.append(int(input()))

dp[0], dp[1], dp[2] = 1, 1, 2

# n개 만큼의 자리가 되는 좌석 수를 구한다. 피보나치 수열
for i in range(3, n+1):
    dp[i] = dp[i-1]+dp[i-2]

answer = 1
if m >= 1: # vip가 1명이라도 있으면 
    pre = 0
    for i in range(m):
        answer *= dp[vip_chairs[i]-1-pre] # 자리의 섹터만큼 길이를 구해서 저장
        pre = vip_chairs[i] # 다음 섹터를 구하기 위해 이전 vip 자리 저장
    answer *= dp[n-pre] # 마지막 섹터 곱해주기

else: # vip가 없을 경우
    answer = dp[n]

print(answer)


