N = int(input())
expression = input()
answer = -2 ** 31

if N == 1:
    print(max(answer, int(expression)))
    exit()

symbol = ["+", "-", "*"]


def add_parenthesis(index, expression_list):
    global answer

    # 최종 값을 구하는 부분
    if index == N:
        for i, j in enumerate(expression_list):
            if len(j) == 3:
                expression_list[i] = str(eval(j))
        result = expression_list[0]
        for _ in range(1, len(expression_list), 2):
            result = eval(str(result) + expression_list[_] + expression_list[_ + 1])

        if answer < result:
            answer = result
        return

    # 다음 식에 괄호를 추가하거나 안하거나 두가지 경우로 넘겨줌

    # 순서대로 한글자씩 추가해서 넘겨준 후 제거
    expression_list.append(expression[index])
    add_parenthesis(index + 1, expression_list)
    del expression_list[-1]

    # 맨마지막이 심볼이면 다음 세자리 추가해서 넘겨 줌.
    if expression_list[-1] in symbol and index + 3 <= N:
        expression_list.append(expression[index:index + 3])
        add_parenthesis(index + 3, expression_list)
        del expression_list[-1]


add_parenthesis(1, [expression[0]])
print(answer)