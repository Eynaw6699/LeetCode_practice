"""
Given a non-negative integer x, return the square root of x rounded down to the nearest integer.
The returned integer should be non-negative as well.

Example 1:

Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.
Example 2:

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.
"""


class Solution(object):
    def mySqrt(self, x):
        res = x
        while res * res - x >= 1:
            res = (res + x / res) / 2
            print(f"res:{res}")
        return int(res)


if __name__ == '__main__':
    main = Solution()
    main.mySqrt(x=4)
