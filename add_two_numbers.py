from typing import Optional
from typing import ListNode
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = dummy = ListNode()
        carry = 0   # 8 + 6 = 14, carry is 1
        while l1 or l2:
            v1, v2 = 0, 0
            if l1: v1, l1 = l1.val, l1.next
            if l2: v2, l2 = l2.val, l2.next
            
            val = carry + v1 + v2
            carry = val // 10   # 8 + 6 = 14, carry = 1
            val = val % 10      # 8 + 6 = 14, val = 4
            res.next = ListNode(val)
            res = res.next
            
        if carry:
            res.next = ListNode(carry)
            
        return dummy.next