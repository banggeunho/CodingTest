def solution(N, stages):
    per_failure = []
    total = len(stages)
    for i in range(1, N+1):
        if total == 0 and i not in stages:
            per_failure.append((i, 0))

        else:
            count = stages.count(i)
            per_failure.append((i, count/total))
            total -= count

    per_failure.sort(key= lambda x: -x[1])
    return list(map(lambda x:x[0], per_failure))

