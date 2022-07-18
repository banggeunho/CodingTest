
'''
3진법으로 생각하여 문제 풀이 (0, 1, 2) 숫자만 사용 가능
하지만, 문제에서는 1, 2, 4만 사용 가능하다고 제한하기 때문에

즉, 0인 경우에는 4로 표현되어야 하기 떄문에 divmod 부분에서 n-1로 입력을 넣어준다.
'''
def solution(n):
    if n <= 3:
        return '124'[n-1]
    
    else:
        q, r = divmod(n-1, 3)
        return solution(q) + '124'[r]