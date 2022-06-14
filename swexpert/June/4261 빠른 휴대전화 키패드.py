keypad = [[],
          ['a','b','c'],
          ['d','e','f'],
          ['g','h','i'],
          ['j','k','l'],
          ['m','n','o'],
          ['p','q','r','s'],
          ['t','u','v'],
          ['w','x','y','z']]

for tc in range(1, int(input())+1):
    S, N = map(int, input().split())
    S = str(S)
    words = list(input().split())
    answer = 0

    for word in words:
        cnt = 0
        for i in range(len(word)):
            if word[i] in keypad[int(S[i]) - 1]:
                cnt += 1
            else:
                break
        if cnt == len(S):
            answer += 1

    print(f'#{tc} {answer}')


# 단순 구현 문제