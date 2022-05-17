# sum 함수를 이용하면 시간초과발생
# 맨 처음 값을 제거하고 다음값을 더해주는 식으로 작성하면 문제 해결
import sys
n, k = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))
result = sum(data[:k])
temp = result
for i in range(k, n):
    temp += data[i]
    temp -= data[i-k]
    # print(result, temp)
    result = max(result, temp)

print(result)

