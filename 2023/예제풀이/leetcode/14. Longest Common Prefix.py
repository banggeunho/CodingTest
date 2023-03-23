# https://leetcode.com/problems/longest-common-prefix/
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        min_str = min(strs, key=len)
        result = ""
        for i in range(len(min_str)):
            valid = True
            for j in range(len(strs) - 1):
                if strs[j][i] != strs[j + 1][i]:
                    valid = False
                    break

            if valid:
                result += strs[0][i]

            if not valid:
                break

        return result