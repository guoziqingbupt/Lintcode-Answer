"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: A Tree
    @return: Postorder in ArrayList which contains node values.
    """
    def postorderTraversal(self, root):

        result = []
        if not root:
            return result

        stack = [root]
        pre = None
        while len(stack) != 0:
            cur = stack[-1]
            if not cur.left and not cur.right:
                pre = cur
                result.append(cur.val)
                stack.pop()
            elif pre and (cur.left is pre or cur.right is pre):
                result.append(cur.val)
                pre = cur
                stack.pop()
            else:
                if cur.right:
                    stack.append(cur.right)
                if cur.left:
                    stack.append(cur.left)
        return result
        # write your code here