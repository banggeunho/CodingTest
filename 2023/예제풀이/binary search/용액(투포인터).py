n = int(input())
arr = list(map(int, input().split()))

start = 0
end = n - 1

result = abs(arr[start] + arr[end])
ans_left = start
ans_right = end

while start < end:
    temp = arr[start] + arr[end]

    if abs(temp) < result:
        result = abs(temp)
        ans_left, ans_right = start, end

        if result == 0:
            break

    if temp < 0:
        start += 1

    else:
        end -= 1

print(arr[ans_left], arr[ans_right])


