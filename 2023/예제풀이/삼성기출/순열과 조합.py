def permutation(arr, r):
    # 순열을 저장할 배열
    result = []

    # 실제 순열을 구하는 함수
    def permute(p, index):
        if len(p) == r:
            result.append(p)
            return

        for idx, data in enumerate(arr):
            if idx not in index:
                # list는 mutable이기 때문에 새로운 리스트를 넘겨준다.
                permute(p + [data], index + [idx])

    permute([], [])

    return result


for r in permutation(['A', 'B', 'C', 'D'], 2):
    print(r)


# 재귀적으로 조합 구현

def combination(arr, r):
    # 조합을 저장할 배열
    result = []

    # 실제 조합을 구하는 함수
    def combinate(c, index):
        if len(c) == r:
            result.append(c)
            return

        for idx, data in enumerate(arr):
            # 중복되는 조합이 생성되지 않게 마지막으로 들어온 원소의 인덱스보다
            # 새로 추가하는 원소의 인덱스가 큰 경우만 조합을 생성한다.
            if idx > index:
                combinate(c + [data], idx)

    combinate([], -1)

    return result


for r in combination(['A', 'B', 'C', 'D'], 2):
    print(r)