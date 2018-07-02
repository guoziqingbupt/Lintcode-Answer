class Solution:
    """
    @param: A: A list of integers
    @param: elem: An integer
    @return: The new length after remove
    """
    def removeElement(self, A, elem):
        index = 0
        while index < len(A):
            if A[index] == elem:
                A.remove(elem)
            else:
                index += 1
        return len(A)
        # write your code here
