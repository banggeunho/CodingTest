# https://leetcode.com/problems/3sum-closest/description/

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        answer = float('INF')
        nums.sort()
        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1

            while left < right:
                sum_value = nums[i] + nums[left] + nums[right]
                # print(nums[i], nums[left], nums[right], sum_value)

                if abs(sum_value - target) < abs(answer - target):
                    answer = sum_value

                if sum_value <= target:
                    left += 1

                elif sum_value > target:
                    right -= 1

        return answer