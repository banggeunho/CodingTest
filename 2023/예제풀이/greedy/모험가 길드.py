# 모험가 길드
# 입력 받은 수를 정렬하여 낮은 숫자부터 하나씩 확인하여
# 그룹에 포함된 모험가의 수가 현재 숫자(공포도) 이상이라면 그룹결성
# 그 후, 다시 새로운 그룹을 만들어 결성
# -> 항상 최소한의 수를 포함하여 그룹을 결성한다
# -> 따라서, 항상 최대한 많은 그룹이 구성되는 방법

n = int(input())
arr = list(map(int, input().split()))

arr.sort()
result = 0
count = 0
for i in arr:
    count += 1 # 현재 그룹에 모험가 포함
    if count >= arr[i]: # 그룹 인원수가 현재 공포도보다 높아지면
        result +=1 # 그룹 결성
        count = 0 # 다음 그룹 인원 모집

print(result)







