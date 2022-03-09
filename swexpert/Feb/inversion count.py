# 코딩테스트 대비 기초 문제 풀이 22일차
# Date : 2022. 02. 07.
# Inversion Count
# https://swexpertacademy.com/main/code/userProblem/userProblemDetail.do?contestProbId=AXpNFir6f24DFATi&categoryId=AXpNFir6f24DFATi&categoryType=CODE
import sys
input = sys.stdin.readline

def mergeSort(rawArr, sortedArr, left, right):
    """
    > 왼쪽부터 bottom up으로 merge해 나가는 함수
    """
    inv_count = 0
    if left < right: 
        mid = (left + right) // 2
        inv_count += mergeSort(rawArr, sortedArr, left, mid)
        inv_count += mergeSort(rawArr, sortedArr, mid + 1, right)
        inv_count += merge(rawArr, sortedArr, left, mid, right)
    return inv_count

def merge(rawArr, sortedArr, left, mid, right):
    """
    > rawArr[left: mid]를 leftSubArray로 두고 
    > rawArr[mid+1: right]를 rightSubArray로 두고
    두 어레이를 merger하는데, 그 과정에서 inversion도 함께 확인한다.
    """
    i = left # leftSubArray의 인덱스
    j = mid + 1 # rightSubArray의 인덱스
    sorted_i = left # sortedArr의 인덱스
    inv_count = 0 # inversion Count

    # i가 left subArray의 구간을 넘지 않는지
    # j가 right subArray의 구간을 넘지 않는지 체크합니다.
    while (i <= mid) and (j <= right):
        if rawArr[i] <= rawArr[j]:
            # 왼쪽 요소가 오른쪽 요소보다 작습니다.
            # 즉, inversion이 아닌 상황이므로 inv_count를 증가시킬 필요가 없죠.
            sortedArr[sorted_i] = rawArr[i]
            i += 1
        elif rawArr[i] > rawArr[j]: 
            # 왼쪽 요소가 오른쪽 요소보다 큽니다.
            # 보통, mergeSort에서 swap이 발생하는 상황이죠. 
            # 그런데, mergeSort에서는 왼쪽 subArray와 오른쪽 subArray가 모두 정렬되어 있는 상황입니다.
            # 따라서, leftSubArray[i:]의 모든 원소들은 당연히 rightSubArray[j]보다 크겠죠. 
            # 즉, leftSubArray[i:]의 수만큼 inversion이 발생한 것이라고 말할 수 있습니다.
            sortedArr[sorted_i] = rawArr[j]
            inv_count += (mid - i + 1) # i번째 뒤부터 중간값까지의 값들은 다 inversion_count이다.
            j += 1
        else: # 이 경우는 존재하지 않음.
            print("Impossible Case")
        sorted_i += 1

    # 남아있는 왼쪽 어레이를 sortedArr에 넣어주고
    while i <= mid:
        sortedArr[sorted_i] = rawArr[i]
        sorted_i += 1
        i += 1
    # 남아있는 오른쪽 어레이를 sortedArr에 넣어준다.
    while j <= right:
        sortedArr[sorted_i] = rawArr[j]
        sorted_i += 1
        j += 1
    # 그리고, 정렬된 애들을 sortedArr에도 그대로 넣어주면 되죠.
    for loop_var in range(left, right + 1):
        rawArr[loop_var] = sortedArr[loop_var]
    return inv_count

t = int(input())

for k in range(t):
  n = int(input())
  arr = list(map(int, input().split()))

  result = mergeSort(arr, [0] * len(arr), 0, len(arr) - 1)

  print(f'#{k+1} {result}')
