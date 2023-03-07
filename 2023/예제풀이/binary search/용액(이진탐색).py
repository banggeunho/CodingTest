import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))

result = float("INF")
ans_left = 0
ans_right = 0

for i in range(n-1):
    current = arr[i]

    start = i + 1
    end = n - 1

    while start <= end:

        mid = (start + end) // 2
        temp = current + arr[mid]

        if abs(temp) < result:
            result = abs(temp)
            ans_left, ans_right = i, mid

            if temp == 0:
                break

        if temp < 0:
            start = mid + 1

        else:
            end = mid - 1

print(arr[ans_left], arr[ans_right])


