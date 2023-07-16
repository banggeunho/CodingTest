# https://school.programmers.co.kr/learn/courses/30/lessons/68935
# v1
def to3(n):
    total = 0
    location = 1
    while n > 0:
        total += location * (n % 3)
        location *= 10
        n //= 3

    return total


def reverse(n):
    return int(str(n)[::-1])


def to10(n):
    total = 0
    location = len(str(n)) - 1
    while n > 0:
        q = n // (10 ** location)
        total += (3 ** location) * q
        print('total', total, 'location', location, 'q', q)

        n %= (10 ** location)
        location -= 1

    return total


def solution(n):
    return to10(reverse(to3(n)))

#v2
def to3(n):
    total = 0
    location = 1
    while n > 0:
        total += location * (n % 3)
        location *= 10
        n //= 3

    return total

def reverse(n):
    return str(n)[::-1]

def solution(n):
    return int(reverse(to3(n)), 3)


#v3
def radixChange(num, radix):
    if num == 0: return '0'
    nums = []
    while num:
        num, digit = divmod(num, radix)
        nums.append(str(digit)) # 나머지 저장

    return ''.join(reversed(nums))

def solution(n):
    return int(radixChange(n, 3)[::-1], 3)