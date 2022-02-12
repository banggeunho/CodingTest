# 코딩테스트 대비 기초 문제 풀이 27일차
# Date : 2022. 02. 13.
# 그리디 문제 풀이

# 모험가 길드
# 입력 받은 수를 정렬하여 낮은 숫자부터 하나씩 확인하여
# 그룹에 포함된 모험가의 수가 현재 숫자(공포도) 이상이라면 그룹결성
# 그 후, 다시 새로운 그룹을 만들어 결성
# -> 항상 최소한의 수를 포함하여 그룹을 결성한다
# -> 따라서, 항상 최대한 많은 그룹이 구성되는 방법
n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0 # 총 그룹 수
count = 0 # 현재 그룹에 포함된 모함가의 수

for i in data: # 공포도를 낮은 것 부터 하나씩 확인
  count += 1 # 현재 그룹에 해당 모함가를 포함시키기
  if count >= i: # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면, 그룹 결성
    result += 1
    count = 0 # 현재 그룹에 포함된 모험가의 수 초기화

print(result)

# 곱하기 혹은 더하기
# 수를 배열로 만들어 결과를 인덱스 0 값으로 설정 후
# 인덱스 1부터 리스트 끝까지 살펴보면서 전 인덱스의 값이 0또는 1이면 
# 더하기를 하도록, 나머지 수들에 대해서는 곱하기를 수행
n = list(map(int, input()))
result = n[0]
for i in range(1, len(n)):

  if n[i-1] == 0 or n[i-1] == 1:
    result = result + n[i]
  
  else:
    result = result * n[i]

print(result)

# 문자열 뒤집기
# 모든 수를 0으로 바꾸는 경우의 수와 1로 바꾸는 경우의 수를 비교하면 끝

arr = list(map(int, input()))

count0 = 0 # 0으로 바꾸는 경우의 수
count1 = 0 # 1로 바꾸는 경우의 수

# 첫번째 수 처리
if arr[0] == 0:
  count1 += 1
else:
  count0 += 1

for i in range(len(arr)-1):
  if arr[i] != arr[i+1]: # 수가 바뀌었을때 카운트를 세어줌
    if arr[i+1] == 0:
      count1 += 1
    else:
      count0 += 1

print(min(count0, count1))
