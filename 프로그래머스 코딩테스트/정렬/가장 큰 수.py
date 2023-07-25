# https://school.programmers.co.kr/learn/courses/30/lessons/42746

from functools import cmp_to_key
def solution(numbers):
    num_strings = list(map(str, numbers))
    num_strings.sort(key = cmp_to_key(lambda x, y: int(x + y) - int(y + x)), reverse=True)
    return str(int(''.join(num_strings)))

def solution(numbers):
    numbers = [str(x) for x in numbers]
    numbers.sort(key = lambda x: x * 3, reverse=True)
    result = ''.join(numbers)

    if '0'* len(numbers) == result:
        return '0'

    else:
        return result
