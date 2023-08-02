n = int(input())
k = int(input())

start = 0
end = k
result = 0
while start <= end:

    mid = (start + end) // 2 # 우리가 찾아야되는 숫자

    cnt = 0 # mid 보다 작거나 같은 갯수
    for i in range(1, n + 1):
        cnt += min(mid // i, n)

    if cnt >= k:
        result = mid
        end = mid - 1

    else:
        start = mid + 1

print(result)





