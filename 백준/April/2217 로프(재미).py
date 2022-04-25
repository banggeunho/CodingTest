n = int(input())
arr = []
result = 0
for _ in range(n):
  arr.append(int(input()))

arr.sort(reverse = True)
for num in range(n):
  result = max(result, arr[num]*(num+1))

print(result)
  