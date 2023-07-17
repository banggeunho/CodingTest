# https://school.programmers.co.kr/learn/courses/30/lessons/72410
def solution(new_id):
    answer = ""

    # 1단계
    s = new_id.lower()
    print(f'1: {s}')

    # 2단계
    filtered = []
    for c in s:
        if (c.isalpha() and c.islower()) or c.isdigit() or c in ('-', '_', '.'):
            filtered.append(c)
    s = ''.join(filtered)
    print(f'2: {s}')

    # 3단계
    temp = ''
    continuous = False
    for c in s:
        if c == '.':
            if not continuous:
                temp += c
                continuous = True
                continue

        else:
            continuous = False
            temp += c
    s = temp
    print(f'3: {s}')

    # 4단계
    if s[0] == ".": s = s[1:]
    if s and s[-1] == ".": s = s[:-1]
    print(f'4: {s}')

    # 5단계
    if not s: s = 'a'
    print(f'5: {s}')

    # 6단계
    if len(s) >= 16: s = s[:15]
    if s[-1] == '.': s = s[:-1]
    print(f'6: {s}')

    # 7단계
    if len(s) <= 2:
        while len(s) < 3:
            s += s[-1]
    print(f'7: {s}')

    return s


print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution("=.="))
print(solution("123_.def"))
print(solution("abcdefghijklmn.p"))
