n = int(input())
arr = list(map(int, input().split()))
arr.sort()
result = arr[len(arr)//2-1] if len(arr) % 2 == 0 else arr[len(arr)//2]
print(result)