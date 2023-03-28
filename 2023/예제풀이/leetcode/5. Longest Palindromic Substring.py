class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 판린드롬 확인 함수
        def isPalindrome(s):
            return s == s[::-1]

        # 결과 저장 변수
        result = ""

        # N^2 탐색
        for i in range(len(s)):

            # 현재 결과가 남은 탐색해야할 문자열보다 길 경우 탐색 종료
            if len(result) > len(s) - i:
                break

            # 임시 문자열
            temp_string = ""

            # 기준 문자에 대해서 문자열을 만들어가며, 판린드롬인지 확인
            for j in range(i + 1, len(s) + 1):

                # 판린드롬일 경우
                if isPalindrome(s[i:j]):
                    # 길이가 임시 문자열보다 길 경우 임시 문자열로 변경
                    if len(s[i:j]) > len(temp_string):
                        temp_string = s[i:j]

            # 결과 갱신
            if len(result) < len(temp_string):
                result = temp_string

        return result