# https://www.acmicpc.net/problem/17609


N = int(input())

for _ in range(N):
    # 입력
    string = input()
    # 확인
    if string == string[::-1]:
        print(0)
        continue

    else:
        count = 0
        start, end = 0, len(string)-1
        while start < end:
            # 양끝에서 가운데로 이동, 같을 경우 다음 자리로 이동
            if string[start] == string[end]:
                start += 1
                end -= 1
            # 다를 경우, 한개 씩 지웠을때 Palindrome이 성립하는지 확인
            else:
                case1_string = string[start+1:end+1]
                case2_string = string[start:end]
                if case1_string == case1_string[::-1] or case2_string == case2_string[::-1]:
                    print(1)
                else:
                    print(2)
                break