'''
짝지어 제거하기 ( 프로그래머스)
https://school.programmers.co.kr/learn/courses/30/lessons/12973

인풋의 갯수가 1,000,000이하의 정수이다.
기본적으로 슬라이딩기법을 사용하면 이중 loop가 사용되기때문에 시간초과가 예상된다.

그러므로 다른 자료구조를 사용해서 생각해보자....
stack을 사용해볼까..? stack이 비어있으면 문자를 넣어주고 
비어있지 않으면 다음에 올 string과 비교를 하는 것이다. 

비교를 했을때 문자가 같으면 stack에서 지워주고, 문자가 같지 않으면 stack 오히려 추가를 하는 것이다.

최종적으로 stack이 비어있으면, 모든 문자열을 인접하여서 제거된 것으로 볼 수 있다.

비어있지 않으면, 문자열이 남아있는 것으로 판별 가능....
'''
def solution(s):
    stack = []
    for i in range(len(s)):
        if not stack:
            stack.append(s[i])
        else:
            if s[i] == stack[-1]:
                stack.pop()
            else:
                stack.append(s[i])

    if stack: return 0
    else: return 1