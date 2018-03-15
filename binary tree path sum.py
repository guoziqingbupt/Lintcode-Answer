"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param: root: the root of binary tree
    @param: target: An integer
    @return: all valid paths
    """

    def binaryTreePathSum(self, root, target):

        sumVal = 0
        result, path = [], []

        self.DFS(root, sumVal, target, path, result)
        return result

    def DFS(self, cur, sumVal, target, path, result):

        if cur is None:
            return

        if cur.left is None and cur.right is None:
            if sumVal + cur.val == target:
                path.append(cur.val)
                result.append(path.copy())

                # recover
                path.pop()

        else:
            sumVal += cur.val
            path.append(cur.val)
            self.DFS(cur.left, sumVal, target, path, result)
            self.DFS(cur.right, sumVal, target, path, result)

            # recover
            path.pop()
            # write your code here

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(4)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(3)

    obj = Solution()
    print(obj.binaryTreePathSum(root, 5))