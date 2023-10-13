# https://www.acmicpc.net/problem/2800
from itertools import combinations

def isInTuple(num, tup):
    for i in range(len(tup)):
        if num in tup[i]:
            return False
    return True

stack = []
string = list(input())
pos = []
for i in range(len(string)):
    if string[i] == '(':
        stack.append(i)
    elif string[i] == ')':
        pos.append((stack.pop(), i))

answer = set()
for i in range(1, len(pos) + 1):
    cases = list(combinations(pos, i))
    for case in cases:
        temp_answer = ""
        for j in range(len(string)):
            if string[j] in '()' and isInTuple(j, case):
                temp_answer += string[j]
            if string[j] not in '()':
                temp_answer += string[j]

        answer.add(temp_answer)

for ans in sorted(list(answer)):
    print(ans)