class Solution(object):
    def fourSum(self, nums, target):
        answer = []
        nums.sort()
        for i in range(len(nums) - 3):
            # 전 숫자랑 같으면 의미 없음 -> continue
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            for j in range(i + 1, len(nums) - 2):
                # 전 숫자랑 같으면 의미 없음 -> continue
                if j > i + 1 and nums[j - 1] == nums[j]:
                    continue
                left, right = j + 1, len(nums) - 1

                while left < right:
                    temp = [nums[i], nums[j], nums[left], nums[right]]
                    sum_value = sum(temp)
                    if sum_value == target:
                        answer.append(temp)
                        # left, right 한칸씩 움직여서 확인
                        left += 1
                        right -= 1
                        # left가 그 전 숫자랑 같은게 있을때까지 left 움직여줌
                        while nums[left] == nums[left-1] and left < right:
                            left += 1
                        # right가 그 전 숫자랑 같은게 있을때까지 right 움직여준다.
                        while nums[right] == nums[right+1] and left < right:
                            right -= 1

                    elif sum_value < target:
                        left += 1

                    else:
                        right -= 1

        return answer