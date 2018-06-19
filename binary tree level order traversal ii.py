"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: A tree
    @return: buttom-up level order a list of lists of integer
    """
    def levelOrderBottom(self, root):
        result = []
        if not root:
            return result

        curList = [root]
        while len(curList) != 0:
            level = []
            tempList = []
            while len(curList) != 0:
                cur = curList.pop(0)
                level.append(cur.val)
                if cur.left:
                    tempList.append(cur.left)
                if cur.right:
                    tempList.append(cur.right)
            result.insert(0, level)
            curList = tempList
        return result
        # write your code here
