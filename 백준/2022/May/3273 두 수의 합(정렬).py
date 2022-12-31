n = int(input())
arr = list(map(int, input().split()))
arr.sort()
x = int(input())
result = 0
for i in range(n):
    if arr[i] < x:
        for j in range(i+1, n):
            if arr[i]+arr[j] == x:
                result += 1
                break

print(result)