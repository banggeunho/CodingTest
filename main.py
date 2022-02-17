# 코딩테스트 대비 기초 문제 풀이 32일차
# Date : 2022. 02. 17.
# 구현 문제 풀이

#-------------------------****----------------------------------
# N의 범위가 500인 경우 : 시간 복잡도가 O(N^3)인 알고리즘을 설계
# N의 범위가 2,000인 경우 : 시간 복잡도가 O(N^2)인 알고리즘을 설계
# N의 범위가 100,000인 경우 : 시간 복잡도가 O(NlogN)인 알고리즘을 설계
# N의 범위가 10,000,000인 경우 : 시간 복잡도가 O(N)인 알고리즘을 설계
#-------------------------****----------------------------------

# 12222. 문자열 나누기

T = int(input())
for test_case in range(1, T + 1):
    s = str(input())
 
    # 1. 가장 좋은 부분 문자열의 길이는 1이다
    # 2. 가능하면 한 글자로 자르고 아니면 한 글자씩 더 붙인다
    # 3. 인접한 문자열이 중복되지 않도록 검사한다 
 
    count = 0
    pre = ""
    idx = 0
    c = ""
 
    while len(s)>idx:
        c += s[idx]
        if c != pre:
            count += 1
            pre = c
            c = ""
         
        idx+=1
 
    print(f"#{test_case} {count}")

# 10580 전봇대

for tc in range(1, int(input())+1):
    N = int(input()) # 전선의 개수
    wires = [list(map(int, input().split())) for i in range(N)]  # 전선 A,B 정보
    cnt = 0 #교점 개수
 
    # 선 두개씩 조합에서 전봇대 두개에서의 높이차의 부호가 같으면 교점이 없다
    for i in range(N):
        for j in range(i+1, N):
            if (wires[i][0]-wires[j][0])*(wires[i][1]-wires[j][1]) < 0:
                cnt += 1
 
    print(f'#{tc} {cnt}')





