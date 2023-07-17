# https://school.programmers.co.kr/learn/courses/30/lessons/70129?language=python3
def removeZero(s):
    return s.replace("0" ,"")

def radixChange(num, radix):
    if num == 0: return '0'
    nums = []
    while num:
        num, digit = divmod(num, radix)
        nums.append(str(digit))
    return ''.join(reversed(nums))

def solution(s):
    answer = []
    remove_cnt = 0
    convert_cnt = 0

    while s != "1":
        # 0 카운트
        for c in s:
            if c == "0":
                remove_cnt += 1

        # 0으로 변환
        s = removeZero(s)
        # 이진 변환
        s = bin(len(s))[2:]
        # s = radixChange(len(s), 2)

        convert_cnt += 1

    return [convert_cnt, remove_cnt]


def solution(s):
    change, zero = 0, 0

    while s != "1":
        change += 1
        num = s.count('1')
        zero += len(s) - num
        s = bin(num)[2:]

    return [change, zero]