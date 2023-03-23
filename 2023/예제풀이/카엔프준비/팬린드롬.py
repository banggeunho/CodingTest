re=[8000, 199992, 11011, 0]


def find_next_palindrome(n, additive):
    l = len(n)
    if l == 0:
        return 0
    first_half = str(int(n[:l // 2 + l % 2]) + additive)
    return int(first_half + first_half[(-1 - l % 2)::-1])


def nearestPalindromic(n):
    m = int(n)

    if m == 0:
        return str(m)

    candidates = [find_next_palindrome(n, additive) for additive in range(2)]  # Cases 1, 2, and 3
    candidates.append(find_next_palindrome("1" + "0" * len(n), 0))  # Case 5

    ans = None
    print(candidates)
    # t는 후보 숫자들
    # m은 기존 숫자
    for t in candidates:
        if ans is None:
            if t - m >= 0:
                ans = t
        else:
            if ans > t and t - m >= 0:
                ans = t
        # print(ans)
    return str(ans)

for re in re:
    print(nearestPalindromic(str(re)))