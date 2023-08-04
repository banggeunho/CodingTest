# https://softeer.ai/practice/info.do?idx=1&eid=414
# P 로봇, H 부품
N, K = map(int, input().split())
arr = list(input())
answer = 0
for i in range(N):
    if arr[i] == 'P':
        for j in range(i - K, i + K + 1):
            if j < 0 or j >= N or j == i:
                continue

            if arr[j] == 'H':
                arr[j] = 'X'
                answer += 1
                break

print(answer)
