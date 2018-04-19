"""
Definition of ListNode

class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param head: n
    @return: The new head of reversed linked list.
    """
    def reverse(self, head):
        if not head:
            return
        pre, cur = None, head

        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        return pre
        # write your code here
