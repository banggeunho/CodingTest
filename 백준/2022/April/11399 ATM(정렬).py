# 11399 ATM
n = int(input())
arr = list(map(int, input().split()))
arr.sort()
result = arr[0]
for i in range(1, n):
    for j in range(i+1):
        result += arr[j]

print(result)