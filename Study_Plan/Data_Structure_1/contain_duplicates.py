from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        new_dict = {}

        for i in nums:
            if i not in new_dict:
                new_dict[i] = 1
            else:
                new_dict[i] += 1

        for k, v in new_dict.items():
            if v > 1:
                return True

        return False


if __name__ == '__main__':
    list_a = [1,2,3,4]
    a = Solution()
    answer = a.containsDuplicate(nums=list_a)
    print(answer)
