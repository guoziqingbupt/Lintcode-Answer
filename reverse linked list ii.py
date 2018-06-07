"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: ListNode head is the head of the linked list
    @param m: An integer
    @param n: An integer
    @return: The head of the reversed ListNode
    """
    def reverseBetween(self, head, m, n):

        left, right = head, head
        pre = ListNode(-1)
        dummy1 = pre
        pre.next = head
        gap = n - m

        for i in range(gap):
            right = right.next
        for i in range(m - 1):
            pre = pre.next
            left = left.next
            right = right.next

        dummy2 = ListNode(-1)
        index = 0
        tail = left
        while index <= gap:
            temp = left.next
            pre.next = temp
            left.next = dummy2.next
            dummy2.next = left
            left = temp
            index += 1

        tail.next = pre.next
        pre.next = dummy2.next

        return dummy1.next
        # write your code here
