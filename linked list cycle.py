"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param: head: The first node of linked list.
    @return: True if it has a cycle, or false
    """
    def hasCycle(self, head):
        slow, fast = head, head

        while fast:

            slow = slow.next
            if fast.next:
                fast = fast.next.next
            else:
                return False

            if fast == slow:
                return True
        return False
        # write your code here
