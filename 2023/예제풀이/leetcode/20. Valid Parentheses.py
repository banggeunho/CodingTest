class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d = {'}': '{', ']': '[', ')': '('}
        stack = []
        for char in s:
            if char in '{[(':
                stack.append(char)

            else:
                if not stack:
                    return False
                else:
                    top = stack.pop()
                    if top != d[char]:
                        return False

        if stack:
            return False
        else:
            return True