#https://programmers.co.kr/learn/courses/30/lessons/42746

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(reverse = True, key = lambda x : x*3)
    return str(int(''.join(numbers)))