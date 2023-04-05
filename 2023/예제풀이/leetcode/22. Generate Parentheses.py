n = 3
result = []

def isValid(s):
    d = {')': '('}
    stack = []
    for char in s:
        if char in '(':
            stack.append(char)

        else:
            if not stack:
                return False
            else:
                top = stack.pop()
                if top != d[char]:
                    return False

    if stack:
        return False
    else:
        return True


def dfs(depth, s):
    if depth == n*2:
        if isValid(s):
            result.append(s)
        return s

    dfs(depth + 1, s + '(')
    dfs(depth + 1, s + ')')

dfs(1, '(')
print(result)
