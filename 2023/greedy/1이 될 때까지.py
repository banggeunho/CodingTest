
n, k = map(int, input().split())
result = 0

# 최대한 많은 나눗셈 연산 실행
while n >= k:
    # 나누어 질 때까지 빼기 연산 실행
    while n % k != 0:
        n -= 1
        result += 1

    # 나누기 연산 실행
    n //= k
    result += 1

# 1이 될때까지 빼기 연산 실행
while n > 1:
    n -= 1
    result += 1

print(result)




