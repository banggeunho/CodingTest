# 코딩테스트 대비 기초 문제 풀이 15일차
# Date : 2022. 02. 02.
# 순차 탐색, 이진 탐색에 대한 원리 공부 및 파이썬 코드로 구현


# 순차 탐색(Sequential Search)이란 리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 차례대로 확인하는 방법이다.
# 시간 복잡도 : Worst-Case -> O(N) // 하나씩 확인해야 하기 때문에

# 순차 탐색 소스코드
# def sequential_search(n, target, array):
#   for i in range(n):
#     if array[i] == target:
#       return i+1

# input_data = input().split()
# n = int(input_data[0])
# target = input_data[1]

# array = input().split()

# print(sequential_search(n, target, array))


# 이진 탐색(Binary Search) : 반으로 쪼개면서 탐색하기
# 시작점, 끝점, 그리고 중간점의 위치를 나타내는 변수 3개를 사용
# 찾으려는 데이터와 중간점 위치에 있는 데이터를 반복적으로 비교


