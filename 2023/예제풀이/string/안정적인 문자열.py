# https://www.acmicpc.net/problem/4889

tc = 1
while True:
    string = input()
    count = 0

    # 테스트 케이스 종료 조건
    if '-' in string:
        break

    # 스택_큐
    stack = []

    # 키 알고리즘
    for i in range(len(string)):
        # 여는 괄호일 경우 스택_큐 추가
        if string[i] == '{':
            stack.append(string[i])

        # 닫는 괄호인 경우
        else:
            # 스택의 top이 여는 괄호이면 스택의 top 제거
            if stack and stack[-1] == '{':
                stack.pop()
            # 아니면, 닫는 괄호 추가
            else:
                stack.append('}')

    # 스택이 빌 때까지
    while stack:
        # 위에서 부터 2개씩 pop
        t1 = stack.pop()
        t2 = stack.pop()

        # 두 문자가 같으면 한 개만 뒤집으면 되기 때문에 +1
        if t1 == t2:
            count += 1
        # 두 문자가 다르면 두 개 다 뒤집어야 함. (올바른 괄호인 경우는 애초에 Stack에 없음)
        else:
            count += 2

    # 결과 출력
    print(f'{tc}. {count}')

    tc += 1

