# https://school.programmers.co.kr/learn/courses/30/lessons/42577
def solution(phone_book):
    headers = {}

    for phone_number in phone_book:
        headers[phone_number] = 1

    for phone_number in phone_book:
        header = ''
        for number in phone_number:
            header += number
            if header in headers and header != phone_number:
                return False

    return True

def solution(phone_book):

    phone_book.sort()
    for p1, p2 in zip(phone_book, phone_book[1:]):
        if p2.startswith(p1):
            return False
    return True


print(solution(["119", "97674223", "1195524421"]))
print(solution(["123","456","789"]))