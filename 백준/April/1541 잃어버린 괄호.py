# 이 문제에선 +,- 밖에 나오지 않으며, 괄호를 어떻게 쳐야 최솟값을 나오는지
# 구하는 문제이다. 즉 -일떄 괄호를 넣어주고 다른 - 가 생기기 전까지만 괄호를
# 넣어주고 다시 -가 생기면 다시 괄호를 넣어주고 계속 반복하면 끝

data = list(input())
arr = []
temp = ''
for i in data:
    if i.isdigit():
        temp += i
    else:
        arr.append(temp)
        temp = ''
        arr.append(i)

# 나머지 값 처리
if temp != '':
    arr.append(temp)

minus, result = 0, 0
in_minus = False
for i in arr:
    if i.isdigit() and not in_minus:
        result += int(i)

    if i.isdigit() and in_minus:
        minus += int(i)

    if i == '-':
        in_minus = True # 변환환
        result -= minus
        minus = 0

if minus != 0:
    result -= minus

print(result)