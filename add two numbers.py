"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param l1: the first list
    @param l2: the second list
    @return: the sum list of l1 and l2
    """
    def addLists(self, l1, l2):
        cur1, cur2 = l1, l2
        carry = 0
        dummy = ListNode(-1)
        cur = dummy

        while cur1 and cur2:
            temp = cur1.val + cur2.val + carry
            carry = temp // 10

            if carry == 0:
                cur.next = ListNode(temp)

            else:
                cur.next = ListNode(temp % 10)
                carry = 1
            cur = cur.next
            cur1 = cur1.next
            cur2 = cur2.next

        while cur1:
            temp = cur1.val + carry
            carry = temp // 10
            if carry == 0:
                cur.next = ListNode(temp)
            else:
                cur.next = ListNode(temp % 10)
            cur = cur.next
            cur1 = cur1.next

        while cur2:
            temp = cur2.val + carry
            carry = temp // 10
            if carry == 0:
                cur.next = ListNode(temp)
            else:
                cur.next = ListNode(temp % 10)
            cur = cur.next
            cur2 = cur2.next

        if carry == 1:
            cur.next = ListNode(1)
        return dummy.next
        # write your code here
