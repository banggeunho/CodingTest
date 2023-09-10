def solution(sequence, k):
    answer = [0, int(1e9)]
    start = end = 0
    sum_total = sequence[start]
    while end < len(sequence):
        # print(start, end, sum_total, answer)

        if sum_total == k:
            if answer[1] == int(1e9) or answer[1] - answer[0] + 1 > end - start + 1:
                answer = [start, end]

        if sum_total >= k:
            sum_total -= sequence[start]
            start += 1

        elif sum_total < k:
            end += 1
            if end <= len(sequence) - 1:
                sum_total += sequence[end]

    return answer


print(solution([1, 2, 3, 4, 5], 7))
print(solution([1, 1, 1, 2, 3, 4, 5], 5))
print(solution([2, 2, 2, 2, 2], 6))