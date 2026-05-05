# Add two non-negative numbers represented by a linked list 
# in reverse order. 
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        stk = []
        carry = 0
        while l1 or l2:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            rv = v1 + v2 + carry
            carry = 1 if rv >= 10 else 0
            if carry:
                rv -= 10
            stk.append(rv)
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        if carry:
            stk.append(carry)
        head = None
        while stk:
            ent = stk.pop()
            head = ListNode(ent, head)
        return head
