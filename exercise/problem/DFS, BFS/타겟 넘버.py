#https://programmers.co.kr/learn/courses/30/lessons/43165
answer = 0
def solution(numbers, target):
    global answer
    dfs(numbers, 0, 0, target)
    return answer


def dfs(numbers, idx, temp, target):
    global answer
    if idx == len(numbers) and temp == target:
        answer += 1
        return

    if idx >= len(numbers):
        return

    dfs(numbers, idx+1, temp+numbers[idx], target)
    dfs(numbers, idx+1, temp-numbers[idx], target)