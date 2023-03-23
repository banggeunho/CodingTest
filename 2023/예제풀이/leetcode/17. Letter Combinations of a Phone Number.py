# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/

from itertools import product
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []

        # 폰 전화기 만들기
        digit_alpha = {}
        ascii_code = ord('a')
        for i in range(2, 10):
            temp = []
            n = 3
            if i == 7 or i == 9:
                n = 4
            for j in range(n):
                temp.append(chr(ascii_code))
                ascii_code += 1
            digit_alpha[str(i)] = temp

        # 입력값이 있을 경우

        result = []
        for i in range(len(digits)):
            result.append(digit_alpha[digits[i]])

        result = list(product(*result))
        answer = []
        for i in result:
            answer.append(''.join(i))

        print(answer)
        return answer