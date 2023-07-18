# https://school.programmers.co.kr/learn/courses/30/lessons/12943

def recur(num, depth):
    if num == 1:
        return depth

    if depth == 500:
        return -1

    if num % 2 == 0:
        return recur(num // 2, depth + 1)
    else:
        return recur(num * 3 + 1, depth + 1)


def solution(num):
    return recur(num, 0)