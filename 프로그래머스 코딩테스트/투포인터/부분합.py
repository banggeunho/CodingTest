# https://www.acmicpc.net/problem/1806
N, S = map(int, input().split())
arr = list(map(int, input().split()))
result = INF = int(1e9)

start = end = cnt = 0
temp_sum = 0
while end < len(arr):
    temp_sum += arr[end]
    while temp_sum >= S:
        result = min(result, end - start + 1)
        temp_sum -= arr[start]
        start += 1
    end += 1

print(result if result != INF else 0)
