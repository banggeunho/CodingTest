# Binary Search
class Solution(object):
    def twoSum(self, nums, target):

        numsWithIndex = [(index, element) for index, element in enumerate(nums)]
        numsWithIndex.sort(key=lambda x: x[1])
        print(numsWithIndex)
        start = 0
        end = len(nums) - 1

        while start <= end:

            result = numsWithIndex[start][1] + numsWithIndex[end][1]

            if result < target:
                start = start + 1

            elif result > target:
                end = end - 1

            elif result == target:
                return [numsWithIndex[start][0], numsWithIndex[end][0]]

        print(start, end)


# Hash
class Solution(object):
    def twoSum(self, nums, target):
        tmp = {}
        for (i, j) in enumerate(nums):
            if (target - j) in tmp:
                return [tmp[target-j], i]
            else:
                tmp[j] = i


