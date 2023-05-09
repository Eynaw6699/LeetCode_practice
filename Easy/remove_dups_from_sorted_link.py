from typing import Optional
from collections import deque

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result = head

        while head and head.next:
            if head.val == head.next.val:
                head.next = head.next.next
            else:
                head = head.next

        return result


if __name__ == "__main__":
    head = None
    for x in [1, 1, 2, 3]:
        head = ListNode(x, next=head)

    result = Solution()
    final_result = result.deleteDuplicates(head=head)
    print(final_result)
