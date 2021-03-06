# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
# Example 1:
#
# Input: haystack = "hello", needle = "ll"
# Output: 2
# Example 2:
#
# Input: haystack = "aaaaa", needle = "bba"
# Output: -1
# Example 3:
#
# Input: haystack = "", needle = ""
# Output: 0

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)