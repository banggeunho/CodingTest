import sys
input = sys.stdin.readline
n = int(input())
alpha = [] # 단어 리스트
alpha_nums = dict() # 단어별 자릿수 리스트

for i in range(n):
    alpha.append(input().rstrip()) # 공백제거

# 단어별 자릿수 위치 확인 및 저장
for i in range(n):
    for j in range(len(alpha[i])):
        if alpha[i][j] in alpha_nums:
            alpha_nums[alpha[i][j]] += 10 ** (len(alpha[i])-j-1)
        else:
            alpha_nums[alpha[i][j]] = 10 ** (len(alpha[i])-j-1)

# 딕셔너리에 있는 모든 값을 가져옵니다.
numList = list(alpha_nums.values())
# 내림차순으로 정렬 후
numList.sort(reverse=True)
# 가장 큰 값부터 9부터 곱해서 결과에 더하기
result = 0
count = 9
for i in numList:
    result += i * count
    count -= 1

print(result)
