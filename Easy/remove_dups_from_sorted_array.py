from typing import List


class Solution:

    @staticmethod
    def removeDuplicates(nums: List[int]) -> int:
        # convert to set so that will give us unique elements,
        # sort it & return the len
        nums[:] = sorted(set(nums))
        return len(nums)


if __name__ == "__main__":
    nums = [1, 1, 2]
    result = Solution.removeDuplicates(nums=nums)
    print(result)
