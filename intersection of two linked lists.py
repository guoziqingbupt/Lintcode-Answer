"""
Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
"""


class Solution:
    """
    @param: headA: the first list
    @param: headB: the second list
    @return: a ListNode
    """
    def getIntersectionNode(self, headA, headB):
        p1, p2 = headA, headB
        count1, count2 = 0, 0

        while p1:
            p1 = p1.next
            count1 += 1

        while p2:
            p2 = p2.next
            count2 += 1

        gap = abs(count2 - count1)
        if count1 > count2:
            fast = headA
            slow = headB
        else:
            fast = headB
            slow = headA
        return self.helper(fast, slow, gap)

    def helper(self, fast, slow, gap):
        for i in range(gap):
            fast = fast.next

        while fast:
            if fast is slow:
                return fast
            fast = fast.next
            slow = slow.next
        return None
        # write your code here
