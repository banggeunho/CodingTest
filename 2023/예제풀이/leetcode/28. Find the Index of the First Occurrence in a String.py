class Solution(object):
    def strStr(self, haystack, needle):

        for i in range(len(haystack)):
            if i + len(needle) <= len(haystack):
                print(needle, haystack[i:i + len(needle)])
                if needle == haystack[i:i + len(needle)]:
                    return i

        return -1



