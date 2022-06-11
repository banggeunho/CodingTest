#D3 - 13732 정사각형 판정
# input에서 주어진 모든 #을 사용해서 정사각형을 이루고 있는지 확인해라
# #이 나온 가장 첫번째 점과 마지막 점의 맨해튼 거리를 계산해서 정사격형 조건에 먼저 부합하는지 확인하고,
# 그 후 그 위치를 이용해서 안쪽에도 #이 채워져있는지 확인해라

for tc in range(1, int(input())+1):
    n = int(input())
    arr = []
    loc = []
    for i in range(n):
        data = list(input())
        arr.append(data)
        for j in range(n):
            if data[j] == '#':
                loc.append((i, j))

    loc.sort()
    # print(loc)
    if loc[0][0] - loc[-1][0] != loc[0][1] - loc[-1][1]:
        print(f'#{tc} no')

    else:
        solve = False
        for i in range(loc[0][0], loc[-1][0]+1):
            for j in range(loc[0][1], loc[-1][1]+1):
                if arr[i][j] != '#':
                    print(f'#{tc} no')
                    solve = True
                    break

            if solve:
                break

        if not solve:
            print(f'#{tc} yes')



