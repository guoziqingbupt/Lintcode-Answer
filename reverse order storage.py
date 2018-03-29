class Solution:
    """
    @param head: the given linked list
    @return: the array that store the values in reverse order
    """
    def reverseStore(self, head):

        result = []
        if not head:
            return result

        cur = head
        while cur:
            result.insert(0, cur.val)
            cur = cur.next
        return result
        # write your code here