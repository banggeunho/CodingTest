from collections import deque
class Solution(object):
    def search(self, nums, target):
        if target not in nums:
            return -1
        q = deque(nums)
        for i in range(len(nums)):
            if target == q.popleft():
                return i


# 정렬이 되어있으나 회전이 조금 되어 있는 조건을 잘 활용해야 함
class Solution(object):
    def search(self, nums, target):

        start, end = 0, len(nums) - 1

        while start <= end:
            mid = (start + end) // 2

            if nums[mid] == target:
                return mid

            if nums[start] <= nums[mid]:
                if nums[start] <= target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1

            else:
                if nums[mid + 1] <= target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1

        return -1
