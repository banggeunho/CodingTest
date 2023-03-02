def solution(s):
    if len(s) == 1:
        return 1

    result = int(1e9)
    for i in range(1, len(s) // 2 + 1):
        previous = s[:i]
        compression = ''
        count = 1
        for j in range(i, len(s), i):
            if previous == s[j:j + i]:
                count += 1
            else:
                compression += str(count) + previous if count >= 2 else previous
                previous = s[j:j + i]
                count = 1

        compression += str(count) + previous if count >= 2 else previous
        result = min(result, len(compression))
    return result