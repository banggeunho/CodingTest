n = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split())

# a 각 시험장에 있는 응시자의 수
# b는 총 감독관, c는 부 감독관
# 총 감독관이 꼭 있어야 하는지
result = 0
for people in a:
    temp = 0
    if people > b:
        temp = people - b
        result += 1
    else:
        result += 1

    if temp > c:
        count = temp//c
        if count*c != temp:
            result += count+1
        else:
            result += count

    elif 0 < temp <= c: # 작으면
        result += 1

print(result)
