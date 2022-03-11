# 코딩테스트 대비 기초 문제 풀이 
# Date : 2022. 03. 11.
# Sorting
#-------------------------****----------------------------------
# N의 범위가 500인 경우 : 시간 복잡도가 O(N^3)인 알고리즘을 설계
# N의 범위가 2,000인 경우 : 시간 복잡도가 O(N^2)인 알고리즘을 설계
# N의 범위가 100,000인 경우 : 시간 복잡도가 O(NlogN)인 알고리즘을 설계
# N의 범위가 10,000,000인 경우 : 시간 복잡도가 O(N)인 알고리즘을 설계
#-------------------------****----------------------------------

# 실패율
# 카카오 2019 신입 공채
def solution(N, stages):
    # 전체 사용자의 수를 가져온다
    total = len(stages)
    # 스테이지 별로 실패율을 담을 list를 선언한다.
    failure_per_stage = []
    # 각 스테이지 별로 현재 몇명이 있는지 확인한다.
    for i in range(1, N+1):
        # 남은 사용자가 없는데, 스테이지에 도달한 사람이 없으면 실패율은 0으로 처리
        if total == 0 and stages.count(i) == 0:
            failure_per_stage.append([i, 0])
            continue

        # 각 스테이지와, 실패율을 list에 추가해준다.
        failure_per_stage.append([i, stages.count(i)/total])
        # 스테이지는 아래에서부터 올라가므로 전의 스테이지에 머물러 있는 사람을 빼주는 작업을 해준다.
        total -= stages.count(i)

    # 실패율은 1번 인덱스에 있으므로 내림차순으로 정렬,
    # 실패율이 같을 경우 스테이지가 낮은 순서부터 출력 -> 오름차순으로 정렬
    f = sorted(failure_per_stage, key= lambda x:(-x[1], x[0]))
    print(f)
    answer = list(map(lambda x: x[0], f))
    return answer

  
    
    