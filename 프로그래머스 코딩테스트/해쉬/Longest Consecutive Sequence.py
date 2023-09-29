# https://leetcode.com/problems/longest-consecutive-sequence
class Solution(object):
    def longestConsecutive(self, nums):
        if not nums:
            return 0

        num_set = set(nums)
        max_length = 0

        for num in num_set:
            # 현재 숫자를 시작점으로 생각
            if num - 1 not in num_set:
                current_num = num
                current_length = 1

                # 현재 숫자에서 시작하는 연속된 시퀀스 길이 계산
                while current_num + 1 in num_set:
                    current_num += 1
                    current_length += 1

                max_length = max(max_length, current_length)

        return max_length