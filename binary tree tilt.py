"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: the root
    @return: the tilt of the whole tree
    """
    def findTilt(self, root):

        self.sumTree(root)

        curNodeList = [root]
        result = 0
        while len(curNodeList) != 0:
            cur = curNodeList.pop(0)
            result += self.helper(cur)
            if cur.left:
                curNodeList.append(cur.left)
            if cur.right:
                curNodeList.append(cur.right)
        return result

    def sumTree(self, root):

        if not root.left and not root.right:
            return root.val

        if root.left:
            root.val += self.sumTree(root.left)
        if root.right:
            root.val += self.sumTree(root.right)
        return root.val

    def helper(self, node):
        if node.left and node.right:
            return abs(node.left.val - node.right.val)
        elif node.left:
            return abs(node.left.val)
        elif node.right:
            return abs(node.right.val)
        else:
            return 0
        # Write your code here
