# 코딩테스트 대비 기초 문제 풀이
# Date : 2022. 11. 6.

#-------------------------****----------------------------------
# N의 범위가 500인 경우 : 시간 복잡도가 O(N^3)인 알고리즘을 설계
# N의 범위가 2,000인 경우 : 시간 복잡도가 O(N^2)인 알고리즘을 설계
# N의 범위가 100,000인 경우 : 시간 복잡도가 O(NlogN)인 알고리즘을 설계
# N의 범위가 10,000,000인 경우 : 시간 복잡도가 O(N)인 알고리즘을 설계
#-------------------------****--------------------------------------------

# input을 사용하면 시간초과가 발생하기 떄문에 sys라이브러리를 import 하여
# sys.stdin.readline을 사용해준다..
# 여러개의 입력 받을 수 있기 때문에 split()을 사용한다.
import sys
stack = []
n = int(sys.stdin.readline())

for i in range(n):

    cmd = sys.stdin.readline().split()

    if cmd[0] == "push":
        stack.append(cmd[1])

    elif cmd[0] == "pop":
        if not stack:
            print(-1)
        else:
            print(stack[-1])
            stack.pop()

    elif cmd[0] == "size":
        print(len(stack))

    elif cmd[0] == "empty":
        print(1 if not stack else 0)

    elif cmd[0] == "top":
        if not stack:
            print(-1)
        else:
            print(stack[-1])
