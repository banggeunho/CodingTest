import copy
from collections import deque

def decimalToBinary(num):
    result = []
    tmp = num
    while tmp > 0:
        rem = tmp % 2
        result.append(str(rem))
        tmp //= 2
    return result[::-1]

def checkRule1(arr):
    for i in range(len(arr)-1):
        find = True
        if arr[i+1] == '1':
            for j in range(i+2, len(arr)):
                if arr[j] != '0':
                    find = False
                    break
            if find:
                return i
    return None

def bfs(num, visited):
    q = deque()
    q.append((num, 0))
    visited.append(decimalToBinary(num))

    while q:
        print(q)
        now, cost = q.popleft()
        if now == 0:
            print(cost)
            break

        now = decimalToBinary(now)
        checkRule = checkRule1(now)

        if checkRule != None:
            tmp = copy.deepcopy(now)
            tmp[checkRule] = '1' if tmp[checkRule] == '0' else '0'
            if tmp not in visited:
                q.append((int(''.join(tmp), 2), cost+1))
                visited.append(tmp)

        now[-1] = '1' if now[-1] == '0' else '0'
        if now not in visited:
            q.append((int(''.join(now), 2), cost+1))
            visited.append(now)


n = int(input())
visited = []
bfs(n, visited)
