# 코딩테스트 대비 기초 문제 풀이 35일차
# Date : 2022. 02. 22.
# 구현 문제 풀이

#-------------------------****----------------------------------
# N의 범위가 500인 경우 : 시간 복잡도가 O(N^3)인 알고리즘을 설계
# N의 범위가 2,000인 경우 : 시간 복잡도가 O(N^2)인 알고리즘을 설계
# N의 범위가 100,000인 경우 : 시간 복잡도가 O(NlogN)인 알고리즘을 설계
# N의 범위가 10,000,000인 경우 : 시간 복잡도가 O(N)인 알고리즘을 설계
#-------------------------****----------------------------------


# 기둥과 보 설치
# 2020 카카오 공채 시험
def checkVal(answer):
    for x, y, con in answer:
    
        # 기둥이면서 바닥에 있으면 가능
        if con == 0:
            if y == 0 or [x-1, y, 1] in answer or [x, y, 1] in answer or [x, y-1, 0] in answer:
                continue
            
            return False

        elif con == 1:
            if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or ([x-1, y, 1] in answer and [x+1, y, 1] in answer):
                continue
            
            return False
        
    return True

def solution(n, build_frame):
    answer = [[]]
    answer.pop()
    # n은 벽면의 크기
    
    for i in build_frame:
        # 0:x, 1:y, 2:기둥0/보1, 3:설치1/삭제0
        x, y, con, op = i[0], i[1], i[2], i[3]
        
        # 설치할 경우
        if op == 1:
            answer.append([x, y, con])
          # 유효성 검사 후 적절하면 정답에 추가
            if not checkVal(answer):
                # print('설치 불가능', i,'///', x, y, con)
                answer.remove([x, y, con])
            
        # 제거할 경우
        else:
            answer.remove([x, y, con])
            if not checkVal(answer):
                # print('제거 불가능', i,'///', x, y, con)
                answer.append([x, y, con])
            

    answer.sort(key=lambda x:(x[0], x[1], x[2]))
    return answer

build_frame = [[0, 0, 0, 1], [2,0,0,1], [4,0,0,1], [0, 1, 1, 1], [1, 1, 1, 1],[2, 1, 1, 1], [3, 1, 1, 1], [2, 0, 0, 0], [1,1,1,0],[2,2,0,1]]
print(solution(5, build_frame))