# 백준 1107 리모컨

n = input() # string으로 입력받는다. (똥포인트)
m = int(input())
isBroken = []
answer = abs(100 - int(n))

def Search_Case(idx=0, tmp=""):
    global answer

    if idx > 0:  # 임시로 만든 숫자에 대해서 최솟값을 구해준다. (똥포인트)
        answer = min(answer, abs(int(tmp) - int(n)) + len(tmp))
        # print(tmp, abs(int(tmp) - int(n)) + len(tmp))

    if idx == 6:  # n이 50만까지 이므로 6자리 달성하면 return
        return

    for j in range(10):  # 부서진 버튼이 아닐경우 계속 진행
        if j not in isBroken:
            Search_Case(idx + 1, tmp + str(j))

if n == "100": # n이 100일 경우 바로 0 출력
    print(0)

elif m == 0: # m이 0일 경우 바로 출력
    answer = abs(100 - int(n))
    print(min(answer, len(n)))

else:
    isBroken = list(map(int, input().split()))
    # 경우의 수 구하기
    Search_Case()
    print(answer)