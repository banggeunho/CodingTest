# https://programmers.co.kr/learn/courses/30/lessons/42748
def solution(array, commands):
    answer = []
    n = len(commands)
    for i, j, k in commands:
        answer.append(sorted(array[i-1:j])[k-1])
    
    return answer