# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import List


class Solution:
    @staticmethod
    def longestCommonPrefix(string_list: List[str]) -> str:
        if not string_list:
            return ""
        m, M, i = min(string_list), max(string_list), 0
        for i in range(0, len(M)):
            if m[i] != M[i]:
                break
        else:
            i += 1
        return m[:i]


if __name__ == "__main__":
    S = ["flower", "flow", "flight"]
    print(Solution.longestCommonPrefix(S))
    S_1 = ["dog", "race car", "car"]
    print(Solution.longestCommonPrefix(S_1))
