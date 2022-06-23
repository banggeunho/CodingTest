arr = list(input())
stack = []
answer = 0
tmp = 1

for i in range(len(arr)):

    if arr[i] == '(':
        stack.append(arr[i])
        tmp *= 2

    elif arr[i] == '[':
        stack.append(arr[i])
        tmp *= 3

    elif arr[i] == ')':
        if not stack or stack[-1] == '[': # 올바른 괄호가 아닐떄
            answer = 0
            break

        if arr[i-1] == '(': # 직전의 괄호가 나왔을 경우 더하기 처리
            answer += tmp

        stack.pop()
        tmp //= 2 # 괄호가 닫힌걸로 처리 곱하기 종료

    else:
        if not stack or stack[-1] == '(': # 올바른 괄호가 아닐떄
            answer = 0
            break

        if arr[i-1] == '[': # 직전의 괄호가 나왔을 경우 더하기 처리
            answer += tmp

        stack.pop()
        tmp //= 3 # 괄호가 닫힌걸로 처리 곱하기 종료

if stack:
    print(0)
else:
    print(answer)



