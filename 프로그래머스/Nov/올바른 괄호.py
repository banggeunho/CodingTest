def solution(s):
    tmp = []
    for i in s:
        if len(tmp) == 0:
            tmp.append(i)
        elif i == ')':
            if '(' in tmp:
                tmp.pop()
        else:
            tmp.append(i)

    if len(tmp) == 0:
        return True
    else:
        return False