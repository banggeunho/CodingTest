# https://leetcode.com/problems/3sum/description/

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        answer = []
        nums.sort()
        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1

            # 중복 제거
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            while left < right:
                sum_value = nums[i] + nums[left] + nums[right]

                if sum_value < 0:
                    left += 1
                elif sum_value > 0:
                    right -= 1
                else:
                    answer.append([nums[i], nums[left], nums[right]])

                    # 중복 제거
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    # 다음 스텝
                    left += 1

        return answer