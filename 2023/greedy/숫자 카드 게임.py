
n, m = map(int, input().split())

result = 0
for i in range(n):
    data = min(list(map(int, input().split())))
    result = max(result, data)

print(result)
