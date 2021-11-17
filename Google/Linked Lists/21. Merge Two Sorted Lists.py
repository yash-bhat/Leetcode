# Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.
#
#
#
# Example 1:
#
#
# Input: l1 = [1,2,4], l2 = [1,3,4]
# Output: [1,1,2,3,4,4]
# Example 2:
#
# Input: l1 = [], l2 = []
# Output: []
# Example 3:
#
# Input: l1 = [], l2 = [0]
# Output: [0]
#
#
# Constraints:
#
# The number of nodes in both lists is in the range [0, 50].
# -100 <= Node.val <= 100
# Both l1 and l2 are sorted in non-decreasing order.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()
        res = dummy

        while l1 or l2:
            a = l1.val if l1 else 101
            b = l2.val if l2 else 101

            if a < b:
                res.next = ListNode(a)
                res = res.next
                l1 = l1.next if l1 else None

            else:
                res.next = ListNode(b)
                res = res.next
                l2 = l2.next if l2 else None

        return dummy.next