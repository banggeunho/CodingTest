# 문자열 문제
# QUEUE 를 이용, 시간복잡도를 어떻게든 쥐어짜내서 줄이기..
# SPLIT 함수와 JOIN함수 공부 필요...
import sys
from collections import deque

for tc in range(int(input())):
    cmds = sys.stdin.readline().rstrip()
    n = int(input())
    data = deque(sys.stdin.readline().rstrip()[1:-1].split(','))
    solve = False

    if n == 0:
        data = deque()

    rvs = 0
    for cmd in cmds:
        if cmd == 'R':
            rvs += 1
        if cmd == 'D':
            if data:
                if rvs % 2 == 0:
                    data.popleft()
                else:
                    data.pop()
            else:
                solve = True
                print('error')
                break

    if not solve:
        if rvs % 2 == 0:
            print('['+','.join(data)+']') #신기하구만
        else:
            data.reverse()
            print('[' + ','.join(data) + ']')  # 신기하구만