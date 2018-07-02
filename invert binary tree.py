"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """
    def invertBinaryTree(self, root):
        if not root:
            return
        curList = [root]

        while len(curList) != 0:
            tempList = []
            while len(curList) != 0:
                cur = curList.pop()
                cur.left, cur.right = cur.right, cur.left

                if cur.left:
                    tempList.append(cur.left)
                if cur.right:
                    tempList.append(cur.right)
            curList = tempList
        return root
        # write your code here
