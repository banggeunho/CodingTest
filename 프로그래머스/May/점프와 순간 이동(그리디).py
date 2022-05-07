# 역순으로 생가갛면된다...
def solution(n):
    cnt = 0
    while n > 0:
        print(n)
        q, r = divmod(n, 2)
        n = q
        if r != 0:  # 2의 배수가 아니면
            cnt += 1  # 1을 빼줘서 2의 배수로 맞춰줌

    return cnt