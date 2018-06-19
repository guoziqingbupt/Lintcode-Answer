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
    @return: Level order a list of lists of integer
    """
    def levelOrder(self, root):
        result = []
        if not root:
            return result

        curList = [root]

        while len(curList) != 0:
            temp = []
            tempList = []
            while len(curList) != 0:
                cur = curList.pop(0)
                temp.append(cur.val)
                if cur.left:
                    tempList.append(cur.left)
                if cur.right:
                    tempList.append(cur.right)
            curList = tempList
            result.append(temp)
        return result
        # write your code here
