for tc in range(int(input())):
    data = list(input())
    left, right = 0, 0
    for i in data:
        if i == '(': left += 1 # 여는 괄호
        elif i == ')': # 닫는 괄호
            if left > right: # 여는 괄호가 닫는 괄호보다 많을때에만 카운트
                right += 1

    # 카운트가 정상적으로 됐고, 여는 괄호와 닫는 괄호가 같은 경우
    if (left + right) == len(data) and left == right:
        print('YES')
    else:
        print('NO')