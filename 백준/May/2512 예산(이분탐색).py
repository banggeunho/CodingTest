n = int(input())
data = list(map(int, input().split()))
m = int(input())

start = 0
end = max(data)

answer = 0
temp_result = 0
while start <= end:
    mid = (start+end) // 2
    result = 0

    for i in data:
        if i <= mid:
            result += i
        else:
            result += mid

    print(mid, result)
    if result <= m:
        answer = mid
        start = mid + 1
    else:
        end = mid - 1

print(answer)