# https://school.programmers.co.kr/learn/courses/30/lessons/12973
def solution(s):
    stack = []
    for alp in s:
        stack.pop() if stack and stack[-1] == alp else stack.append(alp)
    return 0 if stack else 1
