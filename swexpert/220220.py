# 코딩테스트 대비 기초 문제 풀이 34일차
# Date : 2022. 02. 20.
# 구현 문제 풀이

#-------------------------****----------------------------------
# N의 범위가 500인 경우 : 시간 복잡도가 O(N^3)인 알고리즘을 설계
# N의 범위가 2,000인 경우 : 시간 복잡도가 O(N^2)인 알고리즘을 설계
# N의 범위가 100,000인 경우 : 시간 복잡도가 O(NlogN)인 알고리즘을 설계
# N의 범위가 10,000,000인 경우 : 시간 복잡도가 O(N)인 알고리즘을 설계
#-------------------------****----------------------------------

# 6692 다솔이의 월급 상자

for tc in range(1, int(input())+1):
  n = int(input())
  result = 0
  for i in range(n):
    p, x = input().split()
    p = float(p)
    x = int(x)


    result += p*x
  
  print(f'#{tc} {round(result, 6): .6f}')

# 6190 정곤이의 단조 증가하는 수

def is_danjo(x):
    x = str(x)
    for i in range(len(x) - 1):
        if int(x[i]) > int(x[i+1]):
            return False
    return True
 

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))
 
    danjo_num = -1
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            number = A[i] * A[j]
            # 단조 증가 이면서 값이 더 크면 danjo_num 교체
            if (is_danjo(number) == True) and (number > danjo_num):
                danjo_num = number
 
    print(f"#{tc} {danjo_num}")


# 1247. 3일차 최적 경로

import collections
import itertools
import math
tc=int(input())
 

def dist(x1, y1, x2, y2):
    return abs(x1-x2) + abs(y1-y2)
 
 
for t in range(1, tc+1):
    n=int(input())
    customers = list(map(int, input().split()))
    company = []
    company.append(customers[0])
    company.append(customers[1])
    home=[]
    home.append(customers[2])
    home.append(customers[3])
    customers=customers[4:]
    customers=[[customers[i], customers[i+1]] for i in range(0, len(customers), 2)]
    ans=math.inf

    # 고객들 끼리의 모든 경우의 수
    for i in itertools.permutations(customers):
        # 회사에서 고객까지 거리
        temp = dist(company[0], company[1], i[0][0], i[0][1])
        # 고객에서 마지막 고객끼리 거리
        for j in range(0, len(customers)-1):
            temp += dist(i[j][0], i[j][1], i[j+1][0], i[j+1][1])

        # 마지막 고객에서 집까지 거리
        temp += dist(i[-1][0], i[-1][1], home[0], home[1])

        # 거리가 작은 것으로 교체
        ans=min(temp, ans)
 
    print('#{} {}'.format(t, ans))