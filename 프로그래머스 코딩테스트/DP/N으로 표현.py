# https://school.programmers.co.kr/learn/courses/30/lessons/42895

def solution(N, number):
    dp = [set() for i in range(9)]
    for i in range(1, 9):
        case = dp[i]
        # 각 사친연산의 값은 계속 재사용 된다.
        # 이전의 연산들을 보며 순서를 바꿔가며 연산한다.(괄호)
        # 나누는 경우엔 divide by zero와 나머지는 버리는 것을 주의한다.
        case.add(int(str(N) * i))
        for j in range(1, i):
            for op1 in dp[j]:
                for op2 in dp[i - j]:
                    case.add(op1 + op2)
                    case.add(op1 - op2)
                    case.add(op1 * op2)
                    if op1 != 0 and op2 != 0: case.add(op1 // op2)

        if number in case: return i

    return -1