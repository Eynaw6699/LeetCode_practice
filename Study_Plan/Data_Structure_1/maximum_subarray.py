from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxs = nums[0]
        curr = nums[0]
        for i in range(1, len(nums)):
            curr = max(nums[i], curr + nums[i])
            maxs = max(maxs, curr)

        return maxs


if __name__ == '__main__':
    new_nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    solution = Solution()
    a = solution.maxSubArray(nums=new_nums)
    print(a)
