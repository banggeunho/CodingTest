class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        arr = [[] for _ in range(numRows)]
        idx = 0
        while True:

            # 현재 idx가 스트링의 길이가 같을 경우 탈출
            if idx == len(s):
                break

            # 아래로 내려가면서 글자 추가
            for i in range(numRows):
                if idx < len(s):
                    arr[i].append(s[idx])
                    idx += 1

            # 대각으로 올라오면서 글자 추가
            for i in range(numRows-2, 0, -1):
                if idx < len(s):
                    arr[i].append(s[idx])
                    idx += 1

        # 결과 도출
        result = ""
        for data in arr:
            result += ''.join(data)

        return result