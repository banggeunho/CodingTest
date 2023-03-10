# https://interviewnoodle.com/longest-substring-with-k-distinct-characters-in-python-sliding-window-pattern-coding-52e36fd79b96

s = input()

for i in range(1, 27):

    table = dict()

    start, end = 0, 0

    longest = 0

    # end 자리를 하나씩 늘려 테이블에 추가
    for end in range(len(s)):

        newChar = s[end]

        # 문자 테이블에 포함되어 있는지 확인
        if newChar in table.keys():
            table[newChar] += 1
        else:
            table[newChar] = 1

        # 문자 다양성이 주어진 조건보다 클 때, 시작 점을 땡긴다.
        while len(table) > i:
            startChar = s[start]
            start += 1
            table[startChar] -= 1

            # 테이블의 특정 키의 원소가 0일 경우 제거
            if table[startChar] == 0:
                table.pop(startChar)

        # 문자 다양성이 일치할 경우에만 갱신
        if len(table) == i:
            longest = max(longest, end-start+1)

    # 정답 출력
    print(longest)
