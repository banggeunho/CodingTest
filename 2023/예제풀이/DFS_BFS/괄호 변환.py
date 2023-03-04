# u, v로 문자열을 쪼갬
def splitStr(str):
    left_cnt = 0
    right_cnt = 0
    result = []
    for i in range(len(str)):
        if str[i] == ")":
            left_cnt += 1
        else:
            right_cnt += 1

        if left_cnt == right_cnt:
            result.append(str[:i+1]) # 균형잡힌 문자열
            result.append(str[i+1:]) # 나머지 문자열
            break

    return result[0], result[1] # u, v

# 스택을 활용한 올바른 괄호 문자열인지 체크
def checkRight(str):
    if str[0] == ')' or str[-1] == '(':
        return False

    stack = [] # stack에는 열린 괄호만 들어감.
    for i in range(len(str)):
        if str[i] == '(':
            stack.append(str[i])
        else:
            if stack: # 스택이 비어있는데 pop인 경우 False
                stack.pop()
            else:
                return False

    # 모든 작업 처리 후 스택이 비어있지 않다면 False
    if stack:
        return False
    else:
        return True


def solution(p):
    result = ''
    # 주어진 조건에 따라 작성
    # 1. 빈 문자열인 경우, 빈 문자열 반환
    if len(p) == 0:
        return ''

    # 2. 올바른 문자열인 경우, 반환
    if checkRight(p):
        return p

    # 3. 위 두가지가 아닐경우, u, v로 쪼갬
    else:
        u, v = splitStr(p)
        # 3. 올바른 문자열인지 체크
        if checkRight(u):
            result += u
            result += solution(v) # v에 대해 1번부터 재귀적으로 수행

        # 4. u가 올바른 문자열이 아니라면
        else:
            result += "(" + solution(v) + ")"
            for i in range(1, len(u)-1):
                print(u[i])
                if u[i] == '(':
                    result += ')'
                else:
                    result += '('

        return result



print(solution("(()())()"))
print(solution(")("))
print(solution("()))((()"))

