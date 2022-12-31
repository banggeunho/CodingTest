for tc in range(int(input())):
    n, m = map(int, input().split())
    data = list(map(int, input().split()))

    if n == 1: # n이 1이면 무조건 1 출력
        print(1)
        continue

    else:
        for idx in range(n): # 문서에 인덱스도 부여
            data[idx] = (data[idx], idx)
            
        count = 0 # 프린터 순서

        while data:
            isMax = True # 기본으로 최대라고 가정
            a, b = data.pop(0) # 첫번째 문서 pop
            for i, j in data:
                if i > a: # 얘보다 큰게 발견되면 바로 스땁 후 맨 뒤에 추가
                    isMax = False
                    data.append((a, b))
                    break

            if isMax: # 이게 최대값이면 출력(프린트)
                count += 1 # 프린터 된 횟수
                if b == m: # 우리가 원하는 인덱스일 경우 정답 출력
                    print(count)
                    break