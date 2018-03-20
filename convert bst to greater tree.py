"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: the root of binary tree
    @return: the new root
    """
    def convertBST(self, root):
        stack = []
        cur = root
        temp = 0

        while cur or len(stack) != 0:

            if cur:
                stack.append(cur)
                cur = cur.right
            else:
                cur = stack.pop()
                cur.val += temp
                temp = cur.val
                cur = cur.left
        return root
