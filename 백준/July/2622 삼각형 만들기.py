# 합동이면 카운트 하지 않는다는 조건 = 제일 긴 변을 가정하고 풀 수 있음.
# 쉽지만 생각해야 하는 문제


n = int(input())
result = 0
for i in range(1, n):
    for j in range(i, n):
        k = n - (i + j)
        if k < j:
            break

        if i + j > k:
            result += 1

print(result)