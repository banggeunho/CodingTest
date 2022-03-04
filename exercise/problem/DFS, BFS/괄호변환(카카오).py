# 코딩테스트 대비 기초 문제 풀이 
# Date : 2022. 03. 04.
# 구현 문제 풀이
# https://www.acmicpc.net/problem/14502
#-------------------------****----------------------------------
# N의 범위가 500인 경우 : 시간 복잡도가 O(N^3)인 알고리즘을 설계
# N의 범위가 2,000인 경우 : 시간 복잡도가 O(N^2)인 알고리즘을 설계
# N의 범위가 100,000인 경우 : 시간 복잡도가 O(NlogN)인 알고리즘을 설계
# N의 범위가 10,000,000인 경우 : 시간 복잡도가 O(N)인 알고리즘을 설계
#-------------------------****----------------------------------
from collections import deque

# 균형잡힌 괄호 문자열
def checkBal(str):
    if str.count('(') == str.count(')'):
        return True
    else:
        return False

# 두개의 균형잡힌 문자열로 쪼개기 함수
def splitStr(str):
    left_cnt = 0
    right_cnt = 0
    result = []
    for i in range(len(str)):
        if str[i] == ')':
            left_cnt += 1
        else:
            right_cnt += 1
        if left_cnt == right_cnt:
            result.append(str[:i+1])
            result.append(str[i+1:])

    return result[0], result[1]

def checkRight(str):
    if str[0] == ')' or str[-1] == '(':
        return False
    
    q = deque([0])
    while q:
        now = q.popleft()
        for i in range(now, len(str)):
            if i > len(str)-1:
                break
        
            if str[i] == '(':
                q.append(i)
                continue
        
            elif str[i] == ')':
                if q:
                    q.popleft()
                else:
                    return False
            
    if q:
        return False
    else:
        return True
          
def solution(p):
    result = ''
  
    if len(p) == 0:
        return result

    elif checkRight(p):
        return p
    
    else:
        u, v = splitStr(p)
        print(u, v)
        if checkRight(u):
            result += u
            result += solution(v)

        else:
            result += '(' + solution(v) + ')'
            for i in range(1, len(u)-1):
                if u[i] == '(':
                    result += ')'
                else:
                    result += '('
        return result
      
p = "()))((()"
print(solution(p))