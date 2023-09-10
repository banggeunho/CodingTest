# https://www.acmicpc.net/problem/15666

N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()  # 입력된 숫자를 정렬하여 사전 순으로 출력하기 위함
answer = []

def dfs(result):
    if len(result) == M:
        answer.append(result[:])
        return

    for i in range(N):
        if result and result[-1] <= nums[i] or not result:
            result.append(nums[i])
            dfs(result)
            result.pop()

visited = [False] * N
dfs([])  # dfs 함수 호출

unique_results = set(tuple(result) for result in answer)  # 중복 제거

for result in sorted(unique_results):  # 중복이 제거된 결과 출력
    print(" ".join(map(str, result)))